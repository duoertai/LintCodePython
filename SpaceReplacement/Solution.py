class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        count = 0

        for i in range(0, length):
            if string[i] == ' ':
                count += 1

        res = length + 2 * count
        j = res - 1

        for i in range(length - 1, -1, -1):
            if string[i] != ' ':
                string[j] = string[i]
                j -= 1
            else:
                string[j] = '0'
                string[j - 1] = '2'
                string[j - 2] = '%'
                j -= 3

        return res
