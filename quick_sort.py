def quick_sort(left, right, data):
    if left < right:
        p = partition(left, right, data)
        quick_sort(left, p-1, data)
        quick_sort(p+1,right,data)
        return p

def partition(left,right,data):
    a, b, p = left, right, data[left]

    while a<b:
        while data[a] <= p:
            a += 1
        while data[b] > p:
            b -=1
        if a < b:
            data[a],data[b] = data[b],data[a]
    
    data[left] = data[b]
    data[b] = p
    return b

data = [3,1,5,3,7,9,8,4,7]
print('Before Sorting ',data)
quick_sort(0, len(data)-1, data)
print("After sorting ",data)