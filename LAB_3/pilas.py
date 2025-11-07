''' 
Reconocedor de parentesis validos
() "( esto no"
TDD
'''

class Solution:
    def is_valid(self, string):
        stack = []

        for char in string:
            if char == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif char == "(":
                stack.append(char)
        return len(stack) == 0



s = Solution()

assert s.is_valid("()") == True
assert s.is_valid("(") == False
assert s.is_valid(")") == False
assert s.is_valid("(())") == True
assert s.is_valid("(()") == False
assert s.is_valid("()())()") == False
