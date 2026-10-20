#!/usr/bin/env python3

import sys
import argparse
import subprocess
import pyarrow.parquet as pq
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filelist')
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--end', type=int, default=None)
    args = parser.parse_args()

    files = Path(args.filelist).read_text().splitlines()
    files = files[args.start:args.end]
    errors = 0

    for parquet_str in files:
        parquet = Path(parquet_str)
        jsonl = Path(str(parquet).replace('/fineweb2-hq/parquet/', '/source/').replace('/parquet/', '/source/'))
        jsonl = jsonl.parent / (jsonl.stem + '.jsonl.zst')

        if not jsonl.exists():
            print(f"MISSING: {jsonl}")
            errors += 1
            continue

        parquet_rows = pq.ParquetFile(parquet).metadata.num_rows

        result = subprocess.run(f'zstdcat {jsonl} | wc -l', shell=True,
                                capture_output=True, text=True)
        jsonl_lines = int(result.stdout.strip())

        if parquet_rows != jsonl_lines:
            print(f"MISMATCH: {parquet}: parquet={parquet_rows} jsonl={jsonl_lines}")
            errors += 1
        else:
            print(f"ok: {parquet} ({parquet_rows})")

    print(f"\n{len(files)} files checked, {errors} errors")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
