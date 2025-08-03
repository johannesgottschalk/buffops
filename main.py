import argparse
from logic.parser import load_buffs
from logic.parser_csv import load_buffs_from_csv
from logic.validator import validate_buffs
from logic.exporter import export_tsv

def main():
    parser = argparse.ArgumentParser(description="BuffOps CLI with format support")
    parser.add_argument("file", help="Path to buff file")
    parser.add_argument("--format", choices=["yaml", "csv"], default="yaml", help="Input file format (default: yaml)")
    args = parser.parse_args()

    if args.format == "csv":
        buffs = load_buffs_from_csv(args.file)
    else:
        buffs = load_buffs(args.file)

    errors = validate_buffs(buffs)
    if errors:
        print("Validation errors:")
        for error in errors:
            print("-", error)
    else:
        print("All buffs are valid.")
        export_tsv(buffs, "buffs_output.tsv")

if __name__ == "__main__":
    main()
