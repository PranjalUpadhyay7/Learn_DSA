# we have to search a query Q form a list L


# for 1st occurence only
def linear_search(Q,L):
    for i in range(len(L)):
        if Q==L[i]:
            return i
    else:
        return -1
    
# for list containing all occurences
def linear_search_all(Q,L):
    occurences=[]
    for i in range(len(L)):
        if Q==L[i]:
            occurences.append(i)
        
    return occurences
    
    
Q=7
T= [1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15,16,7,8,77,7]
print(linear_search(Q,T))
print(linear_search_all(Q,T))
