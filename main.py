import argparse

def main():
    parser = argparse.ArgumentParser(description="Example program")
    parser.add_argument('--input', required=True, help='Input file')
    parser.add_argument('--output', required=True, help='Output file')
    parser.add_argument('--format', required=True, choices=['json', 'yaml', 'xml'], help='Format of the file')

    args = parser.parse_args()

    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")
    print(f"Format: {args.format}")

if __name__ == "__main__":
    main()
