import math


class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """

    def cosineSimilarity(self, A, B):
        # write your code here
        if A is None or B is None or len(A) == 0 or len(B) == 0 or len(A) != len(B):
            return 2.0

        a = 0
        for i in range(0, len(A)):
            a += A[i] * A[i]

        if a == 0:
            return 2.0

        b = 0
        for i in range(0, len(B)):
            b += B[i] * B[i]

        if b == 0:
            return 2.0

        num = 0
        for i in range(0, len(A)):
            num += A[i] * B[i]

        return num * 1.0 / math.sqrt(a * b)
