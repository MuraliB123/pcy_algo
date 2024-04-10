import pandas as pd
from pcy_algo import pcy_algo

dataset = pd.read_csv("path")
transactions = []
unique_items = set()
for i in range(len(dataset)):
  row_index = i
  row_size  = dataset.loc[row_index,"Item(s)"]
  row_items = []
  for j in range(row_size):
    key = "Item " + str(j+1)
    item_name = dataset.loc[row_index,key]
    item_name = item_name.replace(" ","_")
    item_name = item_name.replace("/","_or_")
    unique_items.add(item_name)
    row_items.append(item_name)
  transactions.append(row_items)

items_to_index = {}
num = 1
for item in unique_items:
  items_to_index[item] = num
  num = num + 1

index_to_items = {}
for key, value in items_to_index.items():
    index_to_items[value] = key
    
num_transactions = []
for row in transactions:
  row_list = []
  for item in row:
    item = item.replace(" ","_")
    item = item.replace("/","_or_")
    item_index = items_to_index[item]
    row_list.append(item_index)
  num_transactions.append(row_list)

print(len(num_transactions))
hash_func_size = 40 
support = 500 # 5 percentage
confidence = 30
basket = pcy_algo(num_transactions,unique_items,hash_func_size,support,confidence)
result = basket.mine_data()
for itemset in result:
  print(itemset)