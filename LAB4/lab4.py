num = int(input("Enter number of users: "))
userData = {}

for i in range(num):
    print()
    name = input("Enter username: ")
    itemCount = int(input("How many items? "))

    itemList = []
    for j in range(itemCount):
        itemName = input(f"Item {j + 1}: ")
        itemList.append(itemName)

    userData[name] = itemList

print("user data:")
for name, itemList in userData.items():
    print(name, "->", itemList)

sharedItems = []
for items in userData.values():
    sharedItems.extend(items)


uniquePool = set(sharedItems)

commonItems = []
uniqueItems = []
itemCounts = {}


for item in uniquePool:
    foundCount = 0
    for items in userData.values():
        if item in items:
            foundCount += 1

print("most popular:")
if itemCounts:
    maxCount = 0
    for val in itemCounts.values():
        if val > maxCount:
            maxCount = val

    for (key, val) in itemCounts.items():
        if val == maxCount:
            print(key)
itemCounts[item] = foundCount

print("common item:")
for item in commonItems:
    print(item)

print("unique item:")
for item in uniqueItems:
    print(item)
