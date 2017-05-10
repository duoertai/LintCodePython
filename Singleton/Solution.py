class Solution:
    # @return: The same instance of this class every time
    temp = None
    @classmethod
    def getInstance(cls):
        # write your code here
        if cls.temp is None:
            cls.temp = Solution()
        return cls.temp
