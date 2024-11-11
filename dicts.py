

from typing import Dict, Any, List, Tuple


def create_inventory(items: List[Any]) -> Dict[Any, int]:
    inventory = {}

    for item in items:

        if item in inventory:
            inventory[item] += 1

        else:
            inventory[item] = 1

    return inventory




def add_items(inventory: Dict[Any, int], items: List[Any]) -> Dict[Any, int]:
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory




def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] < 0:  #para que no me queden numeros negativos
                inventory[item] = 0
        else:
            inventory[item] = 1
    return inventory

print(decrement_items({"wood": 2, "iron": 3, "diamond": 1}, ["wood", "wood", "wood", "iron", "diamond", "diamond"]))



def remove_item(inventory, item):   #FALLA EL TEST, {'wood': -1, 'iron': 2, 'diamond': -1} ESO tiene q devolver

    if item in inventory:
        inventory.pop(item)
        return inventory
    else:
        return inventory





def list_inventory(inventory):
    result = []

    for item, quantity in inventory.items():
        if quantity > 0:
            result.append((item, quantity))

    return result









