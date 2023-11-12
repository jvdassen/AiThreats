import json
import xml.etree.ElementTree as ET


def load_taxonomy(file_path):
    with open(file_path, 'r', encoding='utf-8') as taxonomy_file:
        return json.load(taxonomy_file)


asset_taxonomy = load_taxonomy('data/AssetTaxonomy.json')
threat_taxonomy = load_taxonomy('data/ThreatTaxonomy.json')


def find_category_for_asset(asset_name):
    asset_name_lower = asset_name.lower()
    for asset_entry in asset_taxonomy:
        if asset_entry['Asset'].lower() == asset_name_lower:
            return asset_entry['Category']
    return None


def find_threats_for_category(category):
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


def get_threats_by_asset(asset):
    category = find_category_for_asset(asset)
    asset_with_threat_objects = {'Identified Asset': asset,
                                 'Category': category,
                                 'Threats': []}
    if category:
        threats = find_threats_for_category(category)
        if threats:
            asset_with_threat_objects['Threats'] = threats
    return asset_with_threat_objects


def print_asset_with_threat_objects(asset_with_threat_objects):
    category = asset_with_threat_objects['Category']
    asset = asset_with_threat_objects['Identified Asset']
    if category is not None:
        threats = asset_with_threat_objects['Threats']
        if len(threats) > 0:
            print(f"Identified Asset: {asset}")
            print(f"Category: {category}")
            for threat in threats:
                print("Threat Category:", threat["Threat Category"])
                print("Threat:", threat["Threat"])
                print("Description:", threat["Description"])
                print("Potential Impact:", threat["Potential Impact"])
                print()
        else:
            print(f"No threats found for the asset: {asset}")
    else:
        print(f"No category found for the asset: {asset}. Please check the spelling")


def find_threats(xml_content=None):
    if xml_content is None:
        # Load the XML file with assets
        with open('data/TestFile.xml', 'r', encoding='utf-8') as xml_file:
            xml_content = xml_file.read()


    #print(xml_content)
    root = ET.fromstring(xml_content)

    threats_result = list()
    for obj in root.findall(".//object"):
        asset_name = obj.get('assetname')
        threats_result.append(get_threats_by_asset(asset_name))
    return threats_result
