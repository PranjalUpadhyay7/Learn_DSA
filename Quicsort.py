def Quick_sort(arr, low , high):
    if low < high:
        pi = partition(arr, low, high)
        Quick_sort(arr, low, pi-1)
        Quick_sort(arr, pi+1, high)
    return arr
def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i = i + 1
        while i <= j and arr[j] >= pivot:
            j = j - 1
        if i <= j :
            arr[i], arr[j] = arr[j], arr[i]
        else :
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

a=[45,3,35,56,67,233,1,2,47]
print(Quick_sort(a,0, len(a)-1))