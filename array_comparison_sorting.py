def compare_array(arr1, arr2):
    if len(arr1)!=len(arr2):       #comparing the lengths of the two arrays
        return False
    arr1.sort()                  #sorting 1st array
    arr2.sort()                  #sorting 2nd array
    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:       #comparing each element of both the arrays 
            return False
    return True                    #if none of the false statement above is called then arrays are equal by now 




a1=[1,2,4,5,6,7,8,9,9,9,9]
a2=[1,4,2,5,6,7,8,9,9,9,9]
a3=[13,12,23,23]
a4=[]
a5=[1,2,3,4,5,6,7,8,9,9,9]

print(compare_array(a1,a2))
print(compare_array(a1,a3))
print(compare_array(a1,a4))
print(compare_array(a1,a5))
print(compare_array(a1,a1))