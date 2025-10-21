#
# @lc app=leetcode id=2222 lang=python3
#
# [2222] Number of Ways to Select Buildings
#
# https://leetcode.com/problems/number-of-ways-to-select-buildings/description/
#
# algorithms
# Medium (50.53%)
# Likes:    1047
# Dislikes: 54
# Total Accepted:    49.9K
# Total Submissions: 98.8K
# Testcase Example:  '"001101"'
#
# You are given a 0-indexed binary string s which represents the types of
# buildings along a street where:
# 
# 
# s[i] = '0' denotes that the i^th building is an office and
# s[i] = '1' denotes that the i^th building is a restaurant.
# 
# 
# As a city official, you would like to select 3 buildings for random
# inspection. However, to ensure variety, no two consecutive buildings out of
# the selected buildings can be of the same type.
# 
# 
# For example, given s = "001101", we cannot select the 1^st, 3^rd, and 5^th
# buildings as that would form "011" which is not allowed due to having two
# consecutive buildings of the same type.
# 
# 
# Return the number of valid ways to select 3 buildings.
# 
# 
# Example 1:
# 
# 
# Input: s = "001101"
# Output: 6
# Explanation: 
# The following sets of indices selected are valid:
# - [0,2,4] from "001101" forms "010"
# - [0,3,4] from "001101" forms "010"
# - [1,2,4] from "001101" forms "010"
# - [1,3,4] from "001101" forms "010"
# - [2,4,5] from "001101" forms "101"
# - [3,4,5] from "001101" forms "101"
# No other selection is valid. Thus, there are 6 total ways.
# 
# 
# Example 2:
# 
# 
# Input: s = "11100"
# Output: 0
# Explanation: It can be shown that there are no valid selections.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= s.length <= 10^5
# s[i] is either '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def numberOfWays(self, s: str) -> int:
        countOne = 0 
        countZero = 0 
        count10 = 0
        count01 = 0
        count101 = 0
        count010 = 0

        for char in s:
            if char == '1':
                countOne += 1
                count01 += countZero
                count101 += count10
            else:
                countZero += 1
                count10 += countOne
                count010 += count01
        return count101 + count010

# @lc code=end

