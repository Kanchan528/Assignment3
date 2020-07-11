def interpolation_search(arr, n, x):
    low = 0
    high = n-1 

    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = int(low + ((high-low)/(arr[high]-arr[low])) * (x-arr[low]))

        if low == high:
            if arr[low] == x:
                return low

        if arr[pos] == x:
            return pos

        if arr[pos] > x:
            low = pos+1
        else:
            high = pos-1
    return "Not Found"

list1 = [2,3,4,5,6,7,8,9]
x = 7
result = interpolation_search(list1, len(list1), x)
print("The index of element is ", result)
