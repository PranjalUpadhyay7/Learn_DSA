def compare_array_hashing(arr1,arr2):
    if len(arr1)!=len(arr2):                #comparing length of the arrays 
        return False
    hash_map_arr1={}                        #creating empty dictionary to store the hash values
    for i in arr1:                          #iterate through all the elements of 1st array
        if i in hash_map_arr1:              #if dictionary already contains this element increse its hash value by 1
            hash_map_arr1[i]+=1
        elif i not in hash_map_arr1:        #if dictionary doesnot has this element create the element and give its value 1
            hash_map_arr1[i]=1
    for i in arr2:
        if i not in hash_map_arr1 or hash_map_arr1[i]==0:          #if the hash table doesnot contain this element or the element has 0 hash value return false
            return False
        else:
            hash_map_arr1[i]-=1              #if the hash table has this element and its value is not 0 then decrease its value by 1
    return True                              #by now the arrays must be equal so return true


a1=[1,2,4,5,6,7,8,9,9,9,9]
a2=[1,4,2,5,6,7,8,9,9,9,9]
a3=[13,12,23,23]
a4=[]
a5=[1,2,3,4,5,6,7,8,9,9,9]

print(compare_array_hashing(a1,a2))
print(compare_array_hashing(a1,a3))
print(compare_array_hashing(a1,a4))
print(compare_array_hashing(a1,a5))
print(compare_array_hashing(a1,a1))