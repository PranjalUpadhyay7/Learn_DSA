def insertion_sort(arr):
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            temp=arr[j-1]
            arr[j-1]=arr[j]
            arr[j]=temp
            j-+1
    return arr

a=[45,3,35,56,67,233,1,2,47]
print(insertion_sort(a))