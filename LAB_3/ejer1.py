class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

class Solution:
    def middle_node(self, head):
        conteo = 0

        curr_node = head
        while curr_node # equivalente a != None:
            curr_node = curr_node.next
        middle_pos = conteo // 

     

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

node_1.next = node_2
node_2.next = node_3

s = Solution()
assert s.middle_node(node_1)
