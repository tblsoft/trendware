import json

source = 'products.json'
target = 'qsc-products.json'

# Read the JSON array from the input file
with open(source, 'r') as input_file:
    products_data = json.load(input_file)

# Create the new structure
qsc_products = []
for product in products_data:
    qsc_product = {
        "header": {
            "id": product["id"],
            "action": "update"
        },
        "payload": product

    }
    qsc_products.append(qsc_product)

# Write the new JSON structure to the output file
with open(target, 'w') as output_file:
    json.dump(qsc_products, output_file, indent=4)

print("The new JSON structure has been written to qsc-products.json")