a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# set method can be used to easily solve
print(list(set(a) & set(b)))

# set intersection an also be used, but is longer code
# overlapList = set(a).intersection(set(b))

# print(list(overlapList))
