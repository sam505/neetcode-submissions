class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ')': "(",
            '}': "{",
            ']': "["
        }
        stack = []

        for char in (s):
            if char in valid:
                if stack and valid[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack