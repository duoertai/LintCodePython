class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        # Write your code here
        if A is None and B is None:
            return True

        if A is None or B is None:
            return False

        if len(A) != len(B):
            return False

        count = []
        for i in range(0, 128):
            count.append(0)

        for i in range(0, len(A)):
            count[ord(A[i])] += 1
        for i in range(0, len(B)):
            count[ord(B[i])] -= 1

        for i in range(0, 128):
            if count[i] != 0:
                return False

        return True
