def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

if __name__ == "__main__":
    args = parse_arguments()
    if args.format == 'yaml':
        data = load_yaml(args.input)
        save_yaml(data, args.output)
