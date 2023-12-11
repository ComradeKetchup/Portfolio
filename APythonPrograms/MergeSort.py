def mergesort(list1, list2):

    list3 = []

    for element in list1:
        if element not in list3:
            list3.append(element)

    for element in list2:
        if element not in list3:
            list3.append(element)

    return sorted(list3)


l1 = [1, 2, 4]
l2 = [1, 3, 4]

print(mergesort(l1, l2))
