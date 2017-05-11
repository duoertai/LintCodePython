class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        if len(source) < len(target):
            return -1

        for i in range(0, len(source) - len(target) + 1):
            j = 0

            while j < len(target):
                if target[j] != source[i + j]:
                    break
                j += 1

            if j == len(target):
                return i

        return -1
