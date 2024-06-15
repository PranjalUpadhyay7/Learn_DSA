def Merge_sort(arr, left , right):
    if left == right :
        return [arr[left]]
    mid = (left+right)//2
    left_part= Merge_sort(arr, left, mid )
    right_part= Merge_sort(arr, mid+1, right)
    return merge(left_part, right_part)


def merge(arr , arr2):
    arr3=[]
    i=0
    j=0
    while i <len(arr) and j < len(arr2):
        if arr[i]<= arr2[j]:
            arr3.append(arr[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    while i<len(arr):
        arr3.append(arr[i])
        i+=1
    while j<len(arr2):
        arr3.append(arr2[j])
        j+=1
    return arr3

a=[45,3,35,56,67,233,1,2,47]
print(Merge_sort(a,0, len(a)-1))