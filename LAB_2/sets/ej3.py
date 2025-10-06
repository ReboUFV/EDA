''' 
Implementa una función que reciba dos listas de enteros como parámetros y 
devuelva una lista con los elementos comunes sin repetidos. 
'''

'''
class Solution:
    def common_list(self, list1, list2):
        my_set = set()
        # The max/min(l1, l2, key=len) when the key is = len returns the largest/shortest list by length 
        # we can just iterate up to the length of the shortest list since we look for common values
        for i in range(len(min(list1, list2, key=len))): # O(n) 
            if list1[i] == list2[i] and list1[i] not in my_set:
                my_set.add(list1[i])
        return list(my_set) # O(n) 

 
s = Solution()
assert s.common_list([1,2,3,4], [1,1,3,5,7,8]) == [1,3]
assert s.common_list([], [1,1,3,5,7,8]) == []
assert s.common_list([1,2,3,4,5,6,7], [1]) == [1]

'''

class Solution:
    def common_list(self, list1, list2):
        return list(set(list1) & set(list2)) # The & operator is for intersection 

s = Solution()
assert s.common_list([1,2,3,4], [1,1,3,5,7,8]) == [1,3]
assert s.common_list([], [1,1,3,5,7,8]) == []
assert s.common_list([1,2,3,4,5,6,7], [1]) == [1]

