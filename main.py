import json

def find_threats_for_asset(asset_input):
    # Load the AssetTaxonomy.json file
    with open('AssetTaxonomy.json', 'r', encoding='utf-8') as asset_file:
        asset_taxonomy = json.load(asset_file)

    # Load the ThreatTaxonomy.json file
    with open('ThreatTaxonomy.json', 'r', encoding='utf-8') as threat_file:
        threat_taxonomy = json.load(threat_file)

    # Find the category for the given asset
    category = None
    for asset_entry in asset_taxonomy:
        if asset_entry['Asset'].lower() == asset_input.lower():
            category = asset_entry['Category']
            break

    if category:
        # Find threats related to the category
        threats = []
        for threat_entry in threat_taxonomy:
            if category in threat_entry['Affected assets']:
                threats.append({
                    "Threat Category": threat_entry["Threat Category"],
                    "Threat": threat_entry["Threat"],
                    "Description": threat_entry["Description"],
                    "Potential Impact": threat_entry["Potential Impact"]
                })

        if threats:
            return threats
        else:
            return "No threats found for the category: " + category
    else:
        return "No threats found for the entered asset. Please check the spelling"

if __name__ == '__main__':
    asset_input = input("Enter an asset: ")
    threats = find_threats_for_asset(asset_input)
    if isinstance(threats, str):
        print(threats)
    else:
        for threat in threats:
            print("Threat Category:", threat["Threat Category"])
            print("Threat:", threat["Threat"])
            print("Description:", threat["Description"])
            print("Potential Impact:", threat["Potential Impact"])
            print()