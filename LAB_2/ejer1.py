''' 
Implementa una funcion que reciba una lista y la
devuelva sin duplicados
'''

class Solution:
    def no_duplicates(self, nums): # O(n)
        seen = set()
        for num in nums: # O(n) 
            if num in seen:   
                return True    
            seen.add(num) # O(c) 
        return False
    

s = Solution()
print(s.no_duplicates([1, 1, 1, 3, 3, 4]))

assert s.no_duplicates([1, 1, 1, 3, 3, 4]) == True
assert s.no_duplicates([]) == False 

