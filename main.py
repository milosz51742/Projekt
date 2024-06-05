import json
import jsonschema
from jsonschema import validate

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(f'JSON validation error: {err}')
        return False
    return True

if __name__ == "__main__":
    args = parse_arguments()
    if args.format == 'json':
        data = load_json(args.input)
        # Dodaj walidację schematu JSON, jeśli jest dostępna
