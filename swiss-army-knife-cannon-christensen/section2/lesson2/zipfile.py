import argparse


def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            f"{value} is invalid. Must be a positive integer."
        )
    return ivalue


parser = argparse.ArgumentParser(
    description="Compress files and directories into ZIP archives.",
    epilog="""
Examples:
  python ziptool.py --source docs
  python ziptool.py --source docs --output backup.zip
  python ziptool.py --source docs --compression high --verbose
""",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# Required argument
parser.add_argument(
    "--source",
    required=True,
    help="Path to the source directory"
)

# Optional argument with default
parser.add_argument(
    "-o", "--output",
    default="archive.zip",
    help="Output archive name (default: %(default)s)"
)

# Choices validation
parser.add_argument(
    "-c", "--compression",
    choices=["low", "medium", "high"],
    default="medium",
    help="Compression level (default: %(default)s)"
)

# Custom validation
parser.add_argument(
    "-t", "--threads",
    type=positive_int,
    default=2,
    help="Number of compression threads (default: %(default)s)"
)

# Boolean flag
parser.add_argument(
    "-v", "--verbose",
    action="store_true",
    help="Enable verbose output"
)

# Mutually exclusive flags
group = parser.add_mutually_exclusive_group()

group.add_argument(
    "--overwrite",
    action="store_true",
    help="Overwrite existing archive"
)

group.add_argument(
    "--safe",
    action="store_true",
    help="Prevent overwriting existing archive"
)

args = parser.parse_args()

print("Configuration:")
print(f"Source: {args.source}")
print(f"Output: {args.output}")
print(f"Compression: {args.compression}")
print(f"Threads: {args.threads}")
print(f"Verbose: {args.verbose}")
print(f"Overwrite: {args.overwrite}")
print(f"Safe mode: {args.safe}")