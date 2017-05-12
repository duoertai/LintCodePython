class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        res = []

        if numbers is None or len(numbers) < 3:
            return res

        numbers = sorted(numbers)

        for i in range(0, len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left = i + 1
            right = len(numbers) - 1

            while left < right:
                if numbers[i] + numbers[left] + numbers[right] < 0:
                    left += 1
                elif numbers[i] + numbers[left] + numbers[right] > 0:
                    right -= 1
                else:
                    line = []
                    line.append(numbers[i])
                    line.append(numbers[left])
                    line.append(numbers[right])
                    res.append(line)

                    left += 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1

                    right -= 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1

        return res
