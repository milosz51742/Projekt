import xml.etree.ElementTree as ET

def load_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def convert_to_dict(element):
    return {element.tag: {child.tag: child.text for child in element}}

if __name__ == "__main__":
    args = parse_arguments()
    if args.format == 'xml':
        data = load_xml(args.input)
        data = convert_to_dict(data)
