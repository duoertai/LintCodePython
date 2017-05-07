class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        res = []

        if dictionary is None or len(dictionary) == 0:
            return res

        max = 0

        for s in dictionary:
            if len(s) > max:
                max = len(s)
                res = []
                res.append(s)
            elif len(s) == max:
                res.append(s)

        return res
