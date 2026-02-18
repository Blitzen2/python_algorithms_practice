"""
Problem: Two Sum
Approach: Hash Map (Dictionary)
Time Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
