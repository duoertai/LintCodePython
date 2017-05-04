class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """

    def compareStrings(self, A, B):
        # write your code here
        if self.empty(A) and self.empty(B):
            return True

        if self.empty(B):
            return True

        if self.empty(A):
            return False

        count = []
        for i in range(0, 26):
            count.append(0)

        for i in range(0, len(A)):
            count[ord(A[i]) - ord('A')] += 1

        for i in range(0, len(B)):
            count[ord(B[i]) - ord('A')] -= 1
            if count[ord(B[i]) - ord('A')] < 0:
                return False

        return True

    def empty(self, s):
        if s is None or len(s) == 0:
            return True
        else:
            return False
