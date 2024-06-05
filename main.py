def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    args = parse_arguments()
    if args.format == 'json':
        data = load_json(args.input)
        save_json(data, args.output)
