import argparse
import xml.etree.ElementTree as ET

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
            if args.format == 'xml':
                data = ET.parse(infile).getroot()
                print("XML data loaded successfully")
            else:
                print("Unsupported format for this task")
                return
    except Exception as e:
        print(f"Error reading the input file: {e}")
        return

    # Zapis do pliku
    try:
        with open(args.output, 'w') as outfile:
            if args.format == 'xml':
                tree = ET.ElementTree(data)
                tree.write(outfile)
                print("XML data saved successfully")
            else:
                print("Unsupported format for this task")
    except Exception as e:
        print(f"Error writing the output file: {e}")

if __name__ == "__main__":
    main()
