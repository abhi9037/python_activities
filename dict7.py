# Combine values in python list of dictionaries
from collections import Counter

item_list = [{'item': 'item1', 'amount': 350}, {'item': 'item2', 'amount': 320}, {'item': 'item1', 'amount': 222}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result)
