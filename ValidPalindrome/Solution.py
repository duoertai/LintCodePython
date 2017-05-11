class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        if s is None or len(s) == 0:
            return True

        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.valid(s[left]):
                left += 1
            while left < right and not self.valid(s[right]):
                right -= 1

            if left == right:
                break

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def valid(self, c):
        return (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')
