def linear_search(list1, a):
    for i in range(len(list1)):
        if list1[i] == a:
            return i
    return "Element not found"    

list1 = [2,4,3,7,6,9,1]
result = linear_search(list1, 10)
print("The position of element is ", result)

