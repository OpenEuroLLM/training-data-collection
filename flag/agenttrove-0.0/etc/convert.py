#!/usr/bin/env python3

import argparse
import sys
import os
import pyarrow.parquet as pq
import jsonlines
import zstandard as zstd
from concurrent.futures import ThreadPoolExecutor
import io

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qa_to_text import extract_conversations, format_chatml


def process_chunk(records_chunk):
    buffer = io.BytesIO()
    with jsonlines.Writer(buffer) as writer:
        for record in records_chunk:
            writer.write(record)
    return buffer.getvalue()


def main(infile, outfile, num_threads=4, chunk_size=10000, compression_level=3):
    parquet_file = pq.ParquetFile(infile)
    columns = [c for c in parquet_file.schema_arrow.names if c != 'task_binary']
    all_records = []
    for i in range(parquet_file.num_row_groups):
        all_records.extend(parquet_file.read_row_group(i, columns=columns).to_pylist())

    records = []
    skipped = 0
    for r in all_records:
        convs = extract_conversations(r)
        if convs:
            out = {k: v for k, v in r.items() if k != 'conversations'}
            out['text'] = format_chatml(convs)
            records.append(out)
        else:
            if skipped == 0:
                print(f"WARNING: skipping record with no conversations: {str(r)[:200]}", file=sys.stderr)
            skipped += 1

    if skipped:
        print(f"Skipped {skipped} records with no conversations.", file=sys.stderr)

    chunks = [records[i:i + chunk_size] for i in range(0, len(records), chunk_size)]

    with open(outfile, 'wb') as f:
        cctx = zstd.ZstdCompressor(level=compression_level)
        with cctx.stream_writer(f) as compressor:
            with ThreadPoolExecutor(max_workers=num_threads) as executor:
                for chunk_data in executor.map(process_chunk, chunks):
                    compressor.write(chunk_data)


if __name__ == "__main__":
    print("starting conversion from Parquet to compressed JSONL")
    parser = argparse.ArgumentParser(description='Convert Parquet to compressed JSONL')
    parser.add_argument('--infile', required=True, help='Path to input Parquet file')
    parser.add_argument('--outfile', required=True, help='Path to output compressed JSONL file')
    parser.add_argument('--threads', type=int, default=4, help='Number of threads for processing')
    parser.add_argument('--chunk-size', type=int, default=10000, help='Number of records per chunk')
    parser.add_argument("--compression-level", type=int, default=3, help="Zstd compression level")
    args = parser.parse_args()

    main(args.infile, args.outfile, args.threads, args.chunk_size, args.compression_level)
