class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ["+", "-", "/", "*"]:
                right = stack.pop()
                left = stack.pop()
            
                if token == "+":
                    answer = left + right
                elif token == "-":
                    answer = left - right
                elif token == "*":
                    answer = left * right
                else:
                    answer = int(left / right)
                stack.append(answer)
            else:
                stack.append(int(token))
        
        return stack[0]
