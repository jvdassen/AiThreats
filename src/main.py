from backend.threats_finder import print_asset_with_threat_objects


def main():
    asset_input = input("Enter an asset: ")
    print_asset_with_threat_objects(asset_input)


if __name__ == '__main__':
    main()