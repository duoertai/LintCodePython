class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """

    def hashCode(self, key, HASH_SIZE):
        # write your code here
        if key is None or len(key) == 0:
            return 0

        res = 0
        fac = 1

        for i in range(0, len(key)):
            res += (ord(key[len(key) - 1 - i]) * fac) % HASH_SIZE
            res = res % HASH_SIZE
            fac = (fac * 33) % HASH_SIZE

        return res
