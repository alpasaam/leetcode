#
# @lc app=leetcode id=2615 lang=python3
#
# [2615] Sum of Distances
#
# https://leetcode.com/problems/sum-of-distances/description/
#
# algorithms
# Medium (31.92%)
# Likes:    810
# Dislikes: 95
# Total Accepted:    26.6K
# Total Submissions: 83.3K
# Testcase Example:  '[1,3,1,1,2]'
#
# You are given a 0-indexed integer array nums. There exists an array arr of
# length nums.length, where arr[i] is the sum of |i - j| over all j such that
# nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.
# 
# Return the array arr.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,1,1,2]
# Output: [5,0,3,4,0]
# Explanation: 
# When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0
# - 2| + |0 - 3| = 5. 
# When i = 1, arr[1] = 0 because there is no other index with value 3.
# When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2
# - 0| + |2 - 3| = 3. 
# When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3
# - 0| + |3 - 2| = 4. 
# When i = 4, arr[4] = 0 because there is no other index with value 2. 
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,5,3]
# Output: [0,0,0]
# Explanation: Since each element in nums is distinct, arr[i] = 0 for all
# i.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 
# 
# 
# Note: This question is the same as  2121: Intervals Between Identical
# Elements.
# 
#

# @lc code=start
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        from collections import defaultdict

        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)

        result = [0] * len(nums)

        for indices in index_map.values():
            n = len(indices)
            if n == 1:
                continue

            prefix_sums = [0] * (n + 1)
            for i in range(n):
                prefix_sums[i + 1] = prefix_sums[i] + indices[i]

            for i in range(n):
                left_count = i
                right_count = n - i - 1
                left_sum = prefix_sums[i]
                right_sum = prefix_sums[n] - prefix_sums[i + 1]
                current_index = indices[i]

                result[current_index] = (current_index * left_count - left_sum) + (right_sum - current_index * right_count)

        return result
        
# @lc code=end

