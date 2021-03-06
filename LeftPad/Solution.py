class StringUtils:
    # @param {string} originalStr the string we want to append to
    # @param {int} size the target length of the string
    # @param {string} padChar the character to pad to the left side of the string
    # @return {string} a string
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        # Write your code here
        if size <= len(originalStr):
            return originalStr

        if padChar == ' ':
            return originalStr.rjust(size, padChar)

        res = originalStr

        for i in range(0, size - len(originalStr)):
            res = padChar + res

        return res
