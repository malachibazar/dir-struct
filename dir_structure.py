#!/usr/bin/env python3

import os
import argparse


def list_directories(path, level=0, max_depth: int | None = None):
    for entry in sorted(os.listdir(path)):
        if max_depth and level >= max_depth:
            return
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            print("  " * level + "|-- " + entry)
            list_directories(entry_path, level + 1, max_depth)
        else:
            print("  " * level + "|-- " + entry)


def main():
    parser = argparse.ArgumentParser(
        description="Print the current directory and sub-directory structure."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=os.getcwd(),
        help="Path to the directory to list. Default is the current working directory.",
    )
    parser.add_argument(
        "-d",
        "--depth",
        type=int,
        default=0,
        help="Maximum depth to list. Default is 0 (unlimited).",
    )
    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a directory.")
        return

    print(f"Directory structure for: {args.path}")
    list_directories(args.path, max_depth=args.depth)


if __name__ == "__main__":
    main()
