#!/usr/bin/env python3

import argparse
import sys
import os
import json
import io
import jsonlines
import zstandard as zstd
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qa_to_text import extract_conversations, format_chatml


def read_records(infile):
    dctx = zstd.ZstdDecompressor()
    with open(infile, 'rb') as f, dctx.stream_reader(f) as reader:
        for line in io.TextIOWrapper(reader, encoding='utf-8'):
            line = line.strip()
            if line:
                yield json.loads(line)


def process_chunk(records_chunk):
    buffer = io.BytesIO()
    with jsonlines.Writer(buffer) as writer:
        for record in records_chunk:
            writer.write(record)
    return buffer.getvalue()


def main(infile, outfile, num_threads=4, chunk_size=10000, compression_level=10):
    records = []
    skipped = 0
    for r in read_records(infile):
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

    print(f"Conversion complete! Processed {len(records)} rows, skipped {skipped}.")


if __name__ == "__main__":
    print("starting conversion from openthoughts JSONL.zst (conversations) to text-flattened JSONL.zst")
    parser = argparse.ArgumentParser(description='Convert openthoughts-3 conversations JSONL.zst to ChatML text JSONL.zst')
    parser.add_argument('--infile', required=True, help='Path to input JSONL.zst file')
    parser.add_argument('--outfile', required=True, help='Path to output JSONL.zst file')
    parser.add_argument('--threads', type=int, default=4, help='Number of threads for processing')
    parser.add_argument('--chunk-size', type=int, default=10000, help='Number of records per chunk')
    parser.add_argument("--compression-level", type=int, default=10, help="Zstd compression level")
    args = parser.parse_args()

    main(args.infile, args.outfile, args.threads, args.chunk_size, args.compression_level)
