class BinarySearch:
    def __init__(self, T):
        self.T = T

    def binary_search_iterative(self, l, r, Q):
        while l <= r:
            m = (l + r) // 2
            if self.T[m] == Q:
                return m
            if self.T[m] < Q:
                l = m + 1
            else:
                r = m - 1
        return "NOT FOUND"

    def binary_search_recursive(self, l, r, Q):
        if l <= r:
            mid = (l + r) // 2
            if self.T[mid] == Q:
                return mid
            if self.T[mid] < Q:
                return self.binary_search_recursive(mid + 1, r, Q)
            return self.binary_search_recursive(l, mid - 1, Q)
        return "NOT FOUND"
    
    def binary_search_first_occ(self,l,r,Q):
        while l<=r:
            m = (l+r)//2
            if self.T[m]==Q:
                if m>0 and self.T[m-1]==Q:
                    r=m-1
                else:
                    return m
            elif self.T[m]>Q:
                r=m-1
            else:
                l=m+1
        return "NOT FOUND"
    
    def binary_search_first_occ(self,l,r,Q):
        if l<=r:
            m = (l+r)//2
            if self.T[m]==Q:
                if m>0 and self.T[m-1]==Q:
                    return self.binary_search_first_occ(self, l, m-1,Q)
                else:
                    return m
            elif self.T[m]>Q:
                return  self.binary_search_first_occ(self, l,m-1,Q)
            else:
                return self.binary_search_first_occ(self, m+1,r,Q)
        return "NOT FOUND"
# Example usage:
    

Q=7
T= [1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15,16,7,8,77,7]
# T = [1, 2, 3, 4, 5, 6, 7, 8, 9]
binary_search_instance = BinarySearch(T)

result_iterative = binary_search_instance.binary_search_iterative(0, len(T) - 1, Q)
print("Iterative Binary Search Result:", result_iterative)

result_recursive = binary_search_instance.binary_search_recursive(0, len(T) - 1, Q)
print("Recursive Binary Search Result:", result_recursive)


