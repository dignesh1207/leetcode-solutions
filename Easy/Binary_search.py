# Binary Search
# Easy
# Topics
# Company Tags
# Hints
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in O(log n) time and O(1) space.

# Example 1:

# Input: nums = [-1,0,2,4,6,8], target = 4

# Output: 3
# Example 2:

# Input: nums = [-1,0,2,4,6,8], target = 3

# Output: -1
# Constraints:

# 1 <= nums.length <= 10000.
# -10000 < nums[i], target < 10000
# All the integers in nums are unique.
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums, target, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, target, mid + 1, right)
        else:
            return self.binary_search(nums, target, left, mid - 1)