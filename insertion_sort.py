def insertion_sort(list1):
    for i in range(1, len(list1)):
        valueToInsert = list1[i]
        valuePosition = i

        while valuePosition > 0 and list1[valuePosition-1] > valueToInsert:
            list1[valuePosition] = list1[valuePosition-1]
            valuePosition = valuePosition - 1

        list1[valuePosition] = valueToInsert

list1 = [2, 5, 3, 8, 6, 0]
insertion_sort(list1)
print("The sorted list using insertion sort is ")
print(list1)
