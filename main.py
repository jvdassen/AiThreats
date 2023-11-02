import json

def load_taxonomy(file_path):
    with open(file_path, 'r', encoding='utf-8') as taxonomy_file:
        return json.load(taxonomy_file)

def find_category_for_asset(asset_input, asset_taxonomy):
    asset_input_lower = asset_input.lower()
    for asset_entry in asset_taxonomy:
        if asset_entry['Asset'].lower() == asset_input_lower:
            return asset_entry['Category']
    return None

def find_threats_for_category(category, threat_taxonomy):
    threats = []
    for threat_entry in threat_taxonomy:
        if category in threat_entry['Affected assets']:
            threats.append({
                "Threat Category": threat_entry["Threat Category"],
                "Threat": threat_entry["Threat"],
                "Description": threat_entry["Description"],
                "Potential Impact": threat_entry["Potential Impact"]
            })
    return threats

def main():
    asset_taxonomy = load_taxonomy('AssetTaxonomy.json')
    threat_taxonomy = load_taxonomy('ThreatTaxonomy.json')

    asset_input = input("Enter an asset: ")
    category = find_category_for_asset(asset_input, asset_taxonomy)

    if category:
        threats = find_threats_for_category(category, threat_taxonomy)
        if threats:
            for threat in threats:
                print("Threat Category:", threat["Threat Category"])
                print("Threat:", threat["Threat"])
                print("Description:", threat["Description"])
                print("Potential Impact:", threat["Potential Impact"])
                print()
        else:
            print("No threats found for the category:", category)
    else:
        print("No threats found for the entered asset. Please check the spelling")

if __name__ == '__main__':
    main()