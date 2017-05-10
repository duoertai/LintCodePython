class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        if numbers is None or len(numbers) < 2:
            return []

        res = []
        map = {}

        for i in range(0, len(numbers)):
            if map.has_key(numbers[i]):
                res.append(map[numbers[i]] + 1)
                res.append(i + 1)
                return res
            map[target - numbers[i]] = i

        return res
