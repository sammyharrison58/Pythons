import sys
from pathlib import Path
import argparse


def main() -> int:

    parser = argparse.ArgumentParser(
        description="Detect whether a path exists and whether it is a file or a directory."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="test.txt",
        help="Path to check (default: test.txt)",
    )
    args = parser.parse_args()

    path = Path(args.path)

    if not path.exists():
        print(f"Path does not exist: {path}")
        return 1

    if path.is_file():
        print(f"It exists and is a file: {path}")
    elif path.is_dir():
        print(f"It exists and is a directory: {path}")
    else:
        print(f"Path exists but is neither a regular file nor a directory: {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
