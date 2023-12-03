list1 = [1, 2, 3, 4, 5, 6, 2, 7, 8]
list2 = [5, 6, 7, 8, 9, 6, 11, 12]
list3 = [6, 8, 10, 11, 12, 13, 8, 15, 16]
def find_duplicates(list1, list2, list3):
    duplicates = []

    for element in list1:
        if element in list2 and element in list3 and element not in duplicates:
            duplicates.append(element)

    return duplicates
result = find_duplicates(list1, list2, list3)
print("Duplicates in the three lists:", result)
