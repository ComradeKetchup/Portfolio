a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

newList = []

for element in a:
    if element % 2 == 0:
        newList.append(element)

print(newList)
