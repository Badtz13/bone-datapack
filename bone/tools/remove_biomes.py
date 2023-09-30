import json
import os
import sys


def filter_biomes(filter_words):
    datapack_path = os.path.join(os.path.dirname(__file__), '..')
    json_file_path = os.path.join(datapack_path, 'data', 'minecraft', 'dimension', 'overworld.json')

    with open(json_file_path, 'r') as f:
        data = json.load(f)

    filtered_biomes = []
    for biome_entry in data['generator']['biome_source']['biomes']:
        if all(word.lower() not in biome_entry['biome'].lower() for word in filter_words):
            filtered_biomes.append(biome_entry)

    data['generator']['biome_source']['biomes'] = filtered_biomes

    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_biomes.py <filter_word1> <filter_word2> ...")
        print("Example: python remove_biomes.py warm desert badlands")
        sys.exit(1)

    filter_words = sys.argv[1:]
    filter_biomes(filter_words)
