import json
import os
import sys


def disable_item(item_name):
    # Determine namespace
    if ':' in item_name:
        namespace, item = item_name.split(':', 1)
    else:
        namespace = 'minecraft'
        item = item_name

    # Create directory path if it doesn't exist
    datapack_path = os.path.join(os.path.dirname(__file__), '..')
    directory_path = os.path.join(datapack_path, 'data', namespace, 'recipes')
    os.makedirs(directory_path, exist_ok=True)

    # Create an empty JSON file
    json_file_path = os.path.join(directory_path, f'{item}.json')
    with open(json_file_path, 'w') as f:
        json.dump({}, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python disable.py <item_name>")
        print("Example: python disable.py minecraft:apple")
        sys.exit(1)

    item_name = sys.argv[1]
    disable_item(item_name)
