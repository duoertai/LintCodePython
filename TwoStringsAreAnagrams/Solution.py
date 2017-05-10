class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """

    def anagram(self, s, t):
        # write your code here
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False

        count = []
        for i in range(0, 128):
            count.append(0)

        for i in range(0, len(s)):
            count[ord(s[i])] += 1
        for i in range(0, len(t)):
            count[ord(t[i])] -= 1

        for i in range(0, 128):
            if count[i] != 0:
                return False

        return True
