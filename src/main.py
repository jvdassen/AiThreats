from backend.threats_finder import print_asset_with_threat_objects, find_threats, get_threats_by_asset

if __name__ == '__main__':
    question = input("Would you like to enter a specific asset? ")
    if question.lower() == 'yes':
        asset_input = input("Enter an asset: ")
        asset_with_threat_objects = get_threats_by_asset(asset_input)
        print_asset_with_threat_objects(asset_with_threat_objects)
    else:
        threats = find_threats()
        for threat in threats:
            print_asset_with_threat_objects(threat)
