items = ["apple","banana","apple","banana","mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item found",item)
        break
    unique_item.add(item)