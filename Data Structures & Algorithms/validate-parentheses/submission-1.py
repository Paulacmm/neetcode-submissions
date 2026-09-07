class Solution:
    def isValid(self, s: str) -> bool:
        closing = { ')' : '(', ']' : '[', '}' : '{'}

        stack = []

        for i in s:
            # if it starts with closing, check if the opening is in stack
            if i in closing:
                if stack and stack[-1] == closing[i]:
                    stack.pop()
                else:
                    return False
            # if it starts with opening, add it to the stack
            else:
                stack.append(i)
        
        # return True only if the stack is empty
        return True if not stack else False
