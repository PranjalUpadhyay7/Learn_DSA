
def selection_sort(arr):
    length=len(arr)
    for i in range(length-1):
        mini=i
        for j in range(i, length):
            if arr[j]<arr[mini]:
                mini=j
        temp=arr[i]
        arr[i]= arr[mini]
        arr[mini]=temp

    return arr

a=[45,3,35,56,67,233,1,2,47]
print(selection_sort(a))



