import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Example program")
    parser.add_argument('--input', required=True, help='Input file')
    parser.add_argument('--output', required=True, help='Output file')
    parser.add_argument('--format', required=True, choices=['json', 'yaml', 'xml'], help='Format of the file')

    args = parser.parse_args()

    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")
    print(f"Format: {args.format}")

    # Wczytywanie pliku
    try:
        with open(args.input, 'r') as infile:
            if args.format == 'json':
                data = json.load(infile)
                print("JSON data loaded successfully")
            else:
                print("Unsupported format for this task")
                return
    except Exception as e:
        print(f"Error reading the input file: {e}")
        return

    # Zapis do pliku
    try:
        with open(args.output, 'w') as outfile:
            if args.format == 'json':
                json.dump(data, outfile, indent=4)
                print("JSON data saved successfully")
            else:
                print("Unsupported format for this task")
    except Exception as e:
        print(f"Error writing the output file: {e}")

if __name__ == "__main__":
    main()
