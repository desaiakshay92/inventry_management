from consumables.models import Items, NewItem
from json import dumps,loads
from consumables.serializer import ItemSerilizer,NewItemSerilizer

def total_count(dict_data):
    
    total = 0
    for j in dict_data['item']:
        total = total + int(j['qty'])
    return total

