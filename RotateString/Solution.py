class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        if s is None or len(s) <= 1 or offset % len(s) == 0:
            return

        offset = offset % len(s)
        for i in range(0, offset):
            self.rotate(s)

        return s

    def rotate(self, s):
        c = s[-1]

        for i in range(len(s) - 1, 0, - 1):
            s[i] = s[i - 1]

        s[0] = c

        return
