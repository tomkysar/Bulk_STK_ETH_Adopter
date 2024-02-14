import json

def search_addresses(addresses_file, json_file):

    with open(addresses_file, 'r') as f:
        addresses = f.read().splitlines()

    with open(json_file, 'r') as f:
        data = json.load(f)

    for address in addresses:
        address_lower = address.lower()
        found = False
        for item in data:
            if item.get('USER').lower() == address_lower:
                print(f"{item.get('USER')}, {item.get('NUMBER OF CONTRACTS')}")
                found = True
                break

        if not found:
            pass

search_addresses('addys.txt', 'totals.json')
