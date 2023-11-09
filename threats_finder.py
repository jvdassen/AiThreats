import json
import xml.etree.ElementTree as ET


def load_taxonomy(file_path):
    with open(file_path, 'r', encoding='utf-8') as taxonomy_file:
        return json.load(taxonomy_file)


def find_category_for_asset(asset_name, asset_taxonomy):
    asset_name_lower = asset_name.lower()
    for asset_entry in asset_taxonomy:
        if asset_entry['Asset'].lower() == asset_name_lower:
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
    asset_taxonomy = load_taxonomy('data/AssetTaxonomy.json')
    threat_taxonomy = load_taxonomy('data/ThreatTaxonomy.json')

    # Load the XML file with assets
    with open('data/TestFile.xml', 'r', encoding='utf-8') as xml_file:
        xml_content = xml_file.read()

    #print(xml_content)

    root = ET.fromstring(xml_content)

    for obj in root.findall(".//object"):
        asset_name = obj.get('assetname')
        category = find_category_for_asset(asset_name, asset_taxonomy)

        if category:
            threats = find_threats_for_category(category, threat_taxonomy)
            if threats:
                print(f"Identified Asset: {asset_name}")
                print(f"Category: {category}")
                for threat in threats:
                    print("Threat Category:", threat["Threat Category"])
                    print("Threat:", threat["Threat"])
                    print("Description:", threat["Description"])
                    print("Potential Impact:", threat["Potential Impact"])
                    print()
            else:
                print(f"No threats found for the asset: {asset_name}")
        else:
            print(f"No category found for the asset: {asset_name}. Please check the spelling")


if __name__ == '__main__':
    main()
