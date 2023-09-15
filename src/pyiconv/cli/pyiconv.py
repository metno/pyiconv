#!/usr/bin/env python3
"""
python based 'replacement' for iconv. Helpful in case you need the
encodings only available with libiconv's --enable-extra-encodings compile flag

"""
from __future__ import annotations

import argparse
import sys

from ..lib import ENCODINGS, DEFAULT_TO_ENCODING, DEFAULT_FROM_ENCODING


def main():
    parser = argparse.ArgumentParser(
        description="Python based 'repacement' for iconv; output will be written to stdout."
    )
    parser.add_argument("files", help=" to read", nargs="?")
    parser.add_argument(
        "-f",
        "--from-code",
        help="Specifies the encoding of the input.",
        default=DEFAULT_FROM_ENCODING,
    )
    parser.add_argument(
        "-t", "--to-code", help="Specifies the encoding of the input.", default=DEFAULT_TO_ENCODING
    )
    parser.add_argument("--list", help="list encodings and exit.", action="store_true")

    args = parser.parse_args()
    options = {}
    if args.list:
        for enc in sorted(ENCODINGS):
            print(enc)
        sys.exit(0)

    if args.files:
        options["files"] = [args.files]

    if args.from_code:
        options["from_code"] = args.from_code

    if args.to_code:
        options["to_code"] = args.to_code

    for _file in options["files"]:
        # reconfigure stdout to new encoding
        sys.stdout.reconfigure(encoding=options["to_code"], errors="ignore")
        with open(_file, "r", encoding=options["from_code"]) as infile:
            for line in infile:
                print(line.strip())


if __name__ == "__main__":
    main()
