#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Medium (56.82%)
# Likes:    881
# Dislikes: 1038
# Total Accepted:    113K
# Total Submissions: 198.8K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# You are given n points in the plane that are all distinct, where points[i] =
# [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance
# between i and j equals the distance between i and k (the order of the tuple
# matters).
# 
# Return the number of boomerangs.
# 
# 
# Example 1:
# 
# 
# Input: points = [[0,0],[1,0],[2,0]]
# Output: 2
# Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and
# [[1,0],[2,0],[0,0]].
# 
# 
# Example 2:
# 
# 
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: points = [[1,1]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# n == points.length
# 1 <= n <= 500
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# All the points are unique.
# 
# 
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        
        for i in range(len(points)):
            distance_count = {}
            for j in range(len(points)):
                if i == j:
                    continue
                dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                distance_count[dist] = distance_count.get(dist, 0) + 1
            
            for count in distance_count.values():
                if count > 1:
                    result += count * (count - 1)
        
        return result

        
# @lc code=end

