import json
import os
import sys


def copy_and_replace_biome(biome_to_copy, biome_to_insert):
    datapack_path = os.path.join(os.path.dirname(__file__), '..')
    json_file_path = os.path.join(datapack_path, 'data', 'minecraft', 'dimension', 'overworld.json')

    with open(json_file_path, 'r') as f:
        data = json.load(f)

    biomes = data.get("generator", {}).get("biome_source", {}).get("biomes", [])
    new_biomes = []

    for biome in biomes:
        new_biomes.append(biome)
        if biome.get("biome", "") == biome_to_copy:
            new_entry = biome.copy()
            new_entry["biome"] = biome_to_insert
            new_biomes.append(new_entry)

    data["generator"]["biome_source"]["biomes"] = new_biomes

    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python insert_biome.py <biome_to_copy> <biome_to_insert>")
        sys.exit(1)

    biome_to_copy = sys.argv[1]
    biome_to_insert = sys.argv[2]
    
    copy_and_replace_biome(biome_to_copy, biome_to_insert)
