// Two Sum
// Solved 
// Easy
// Topics
// Company Tags
// Hints
// Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

// You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

// Return the answer with the smaller index first.

// Example 1:

// Input: 
// nums = [3,4,5,6], target = 7

// Output: [0,1]
// Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

// Example 2:

// Input: nums = [4,5,6], target = 10

// Output: [0,2]
// Example 3:

// Input: nums = [5,5], target = 10

// Output: [0,1]
// Constraints:

// 2 <= nums.length <= 1000
// -10,000,000 <= nums[i] <= 10,000,000
// -10,000,000 <= target <= 10,000,000
// Only one valid answer exists.

#Time Complexity: O(n^2)
#Space Complexity: O(1)

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

        for(let i =0; i<nums.length; i++){

            for(let j=0; j<nums.length; j++){
                if(i == j) continue;
                if(nums[i]+nums[j]==target){
                    if(i<=j){
                        return [i, j];
                    }
                    else return [j, i];
                }
                else continue;
            }
        }

    }

}

#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, x in enumerate(nums):
            complement = target - x
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[x] = i


            