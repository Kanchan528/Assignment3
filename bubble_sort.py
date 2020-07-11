def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(0, len(list1)-i-1):
            if list1[j] > list1[j+1]:
                (list1[j], list1[j+1]) = (list1[j+1], list1[j]) 
    return list1

list1 = [-2, 5, 0, 11, -9, 3]
print("Sorted list using bubble sort is ",bubble_sort(list1))

