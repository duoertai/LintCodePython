class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        if str is None or len(str) <= 1:
            return True

        count = []
        for i in range(0, 128):
            count.append(0)

        for i in range(0, len(str)):
            count[ord(str[i])] += 1
            if count[ord(str[i])] > 1:
                return False

        return True
