import csv

def load_inventory(filename):
    inventory = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            inventory.append(row)
    return inventory

def save_inventory(filename, inventory):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['product', 'quantity', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory)

filename = 'inventory.csv'
inventory = load_inventory(filename)
for item in inventory:
    print(item)
# Add, modify, or delete items here
save_inventory(filename, inventory)
