def sentinel_search(arr, n , x):
    last = arr[-1]
    arr[-1]=x
    i=0
    while arr[i]!=x:
        i+=1
    arr[-1]=last
    if i<n or arr[-1]==x:
        return i
    else:
        return -1

Q=7
T= [1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15,16,7,8,77,7]
print(sentinel_search(T,len(T),Q))