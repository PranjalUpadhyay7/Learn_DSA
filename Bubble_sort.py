def bubble_sort(arr):
    length = len(arr)
    for i in range(length-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
a=[45,3,35,56,67,233,1,2,47]
print(bubble_sort(a))
    
    