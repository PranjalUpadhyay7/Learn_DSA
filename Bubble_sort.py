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
    
# this type of sorting starts with placing the largest element at the end and proceed by adding sorted terms in decending order 
#it finds largest element and keep swaping till it reaches at end 
#then it find second largest element keep swaping till it reaches last second position
#and similarly for every element it find largest element and keep swaping till it places it on its correct position