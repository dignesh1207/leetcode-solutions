# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()  # Space: O(n)

        for n in nums: # O(n)
            if n in seen:  # O(1)
                return True
            seen.add(n) # O(1)
        
        return False

