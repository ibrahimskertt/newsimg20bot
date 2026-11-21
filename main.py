#!/usr/bin/env python3
"""
main.py - Competition entry deployment script for news-image-20261120.
Python 3.13, Standard Library Only (no external dependencies).

Approach:
1. Locates entry.png in the same directory as this script.
2. Reads entry.png as raw binary bytes.
3. Determines the output directory from the MAKEFUN_OUTPUT_DIR environment variable,
   falling back to '/output' if not set.
4. Ensures the target output directory exists (creating parent directories as needed).
5. Writes the exact binary bytes of entry.png to the target path (<output_dir>/entry.png).
"""

import os
from pathlib import Path

def main() -> None:
    # Locate script directory and entry.png
    script_dir = Path(__file__).resolve().parent
    source_path = script_dir / "entry.png"

    if not source_path.is_file():
        raise FileNotFoundError(f"Required entry poster not found at {source_path}")

    # Determine output directory
    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_env)

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    dest_path = output_dir / "entry.png"

    # Read binary bytes and write unchanged
    poster_bytes = source_path.read_bytes()
    dest_path.write_bytes(poster_bytes)

    print(f"Successfully deployed entry.png ({len(poster_bytes)} bytes) to {dest_path}")

if __name__ == "__main__":
    main()
