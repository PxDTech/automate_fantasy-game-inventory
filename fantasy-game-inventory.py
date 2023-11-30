def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        #print(item)
        if item not in inventory.keys():
            inventory.update({item: 0})
        if item in inventory.keys():
            new_value = inventory.get(item)
            new_value += 1
            inventory[item] = new_value
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
#print(inv)
displayInventory(inv)