from functools import lru_cache

#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (61.91%)
# Likes:    5272
# Dislikes: 184
# Total Accepted:    338.2K
# Total Submissions: 546.1K
# Testcase Example:  '1\n6\n3'
#
# You have n dice, and each dice has k faces numbered from 1 to k.
# 
# Given three integers n, k, and target, return the number of possible ways
# (out of the k^n total ways) to roll the dice, so the sum of the face-up
# numbers equals target. Since the answer may be too large, return it modulo
# 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.
# 
# 
# Example 2:
# 
# 
# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# 
# 
# Example 3:
# 
# 
# Input: n = 30, k = 30, target = 500
# Output: 222616187
# Explanation: The answer must be returned modulo 10^9 + 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n, k <= 30
# 1 <= target <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(rolls_left: int, rem: int) -> int:
            if rem == 0 and rolls_left == 0:
                return 1
            if rolls_left == 0:
                return 0
            res = 0
            for face in range(1, k + 1):
                res += dp(rolls_left - 1, rem - face)
            return res % MOD

        return dp(n, target)
        
# @lc code=end

