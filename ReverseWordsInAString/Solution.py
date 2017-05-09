class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        if s is None:
            return s
        s = s.strip()

        if len(s) == 0:
            return ""

        res = ""

        start = 0
        end = 0

        while end < len(s):
            while end < len(s) and s[end] != ' ':
                end += 1

            res = " " + s[start:end] + res

            if end == len(s):
                break

            while end < len(s) and s[end] == ' ':
                end += 1

            start = end

        return res[1:]