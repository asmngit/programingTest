#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (52.67%)
# Likes:    6680
# Dislikes: 2248
# Total Accepted:    2.3M
# Total Submissions: 4.4M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is palindrome integer.
# 
# An integer is a palindrome when it reads the same backward as forward.
# 
# 
# For example, 121 is a palindrome while 123 is not.
# 
# 
# 
# Example 1:
# 
# 
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# 
# 
# Example 2:
# 
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without converting the integer to a string?
#

# @lc code=start

class Solution:
    def isPalindrome(self, x: int) -> bool:
            sX = str(x)
            aX = list(sX)
            # reverseは、直接配列の中身を逆さにする為、変数に入れる必要がない
            aX.reverse()
            sXR = [str(n) for n in aX]
            reverseJoinAX = "".join(sXR)
            if(sX == reverseJoinAX) :
                return True
            else :
                return False


# @lc code=end

