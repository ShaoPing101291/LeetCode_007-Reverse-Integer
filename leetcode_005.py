# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.



class Solution(object):
    def longestPalindrome(self, s):

        """
        :type s: str
        :rtype: str
        """
        def expand(left, right):
            while True:
                if left < 0 or right >= len(s) or s[left] != s[right]:
                    break
                left-=1
                right +=1
            return s[left + 1:right]

        longest = ""
        for i in range (len(s)):

            odd = expand (i, i)
            even = expand(i, i+1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest
        