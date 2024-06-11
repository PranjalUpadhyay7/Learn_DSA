
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

#in this sort we keep adding smallest element and swap it with very first unsorted position
#we find smallest element and swap it with first element , then find smallest element in remaining unsorted list and swap it with second element 
#similarly we do for all other elements and at last list get sorted


