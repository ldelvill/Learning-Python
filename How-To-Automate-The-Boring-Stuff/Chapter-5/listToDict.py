# fucntion that addes items to your inventory


def displayInventories(inventory):
    print("Inventory:")
    itemTotal = 0

    for k, v in inventory.items():
        print(str(v) + " " + k)
        itemTotal += v

    print("Total number of items: " + str(itemTotal))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
addToInventory(inv, dragonLoot)
displayInventories(inv)
