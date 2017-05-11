class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here

        if s is None or len(s) == 0:
            return True

        stack = []

        for i in range(0, len(s)):
            c = s[i]

            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            elif c == ']':
                if len(stack) == 0:
                    return False

                if stack[-1] != '[':
                    return False

                stack.pop()
            elif c == '}':
                if len(stack) == 0:
                    return False

                if stack[-1] != '{':
                    return False

                stack.pop()
            elif c == ')':
                if len(stack) == 0:
                    return False

                if stack[-1] != '(':
                    return False

                stack.pop()

        return len(stack) == 0
