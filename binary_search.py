def binary_search(list1, left, right, a):
    if right >= left:
        mid = left+(right-left)//2

        if list1[mid] == a:
            return mid

        elif list1[mid] > a:
            return binary_search(list1, 1, mid-1, a)
        else:
            return binary_search(list1, mid+1, right, a)

    else:
        return "Element not present"

list1 = [2,3,4,5,6,7,8]
a = 6
result = binary_search(list1, 0, len(list1)-1, a)
print("The index of element is ",result) 