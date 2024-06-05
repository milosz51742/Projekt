def save_xml(data, file_path):
    tree = ET.ElementTree(data)
    tree.write(file_path)

def convert_to_element(data, root_tag):
    root = ET.Element(root_tag)
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    return root

if __name__ == "__main__":
    args = parse_arguments()
    if args.format == 'xml':
        data = load_xml(args.input)
        data = convert_to_dict(data)
        data_element = convert_to_element(data, 'root') 
        save_xml(data_element, args.output)
