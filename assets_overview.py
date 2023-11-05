import json


def load_taxonomy(file_path):
    with open(file_path, 'r', encoding='utf-8') as taxonomy_file:
        return json.load(taxonomy_file)


def main():
    asset_taxonomy = load_taxonomy('AssetTaxonomy.json')
    count = 0
    for entry in asset_taxonomy:
        asset = entry.get('Asset')
        if asset:
            print()
            print(asset)
            count += 1
    print("There are " + str(count) + " assets!")


if __name__ == '__main__':
    main()
