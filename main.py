import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program description.')
    parser.add_argument('--input', type=str, required=True, help='Input file path')
    parser.add_argument('--output', type=str, required=True, help='Output file path')
    parser.add_argument('--format', type=str, choices=['json', 'yaml', 'xml'], required=True, help='File format')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(f'Input file: {args.input}')
    print(f'Output file: {args.output}')
    print(f'Format: {args.format}')
