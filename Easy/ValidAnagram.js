// Valid Anagram
// Solved 
// Easy
// Topics
// Company Tags
// Hints
// Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

// An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

// Example 1:

// Input: s = "racecar", t = "carrace"

// Output: true
// Example 2:

// Input: s = "jar", t = "jam"

// Output: false
// Constraints:

// s and t consist of lowercase English letters.

#Time Complexity: O(n log n) due to sorting
#Space Complexity: O(n) due to the sorted strings


class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
    if (s.length !== t.length) return false;
    
    const sortedS = s.split('').sort().join('');
    const sortedT = t.split('').sort().join('');

    return sortedS === sortedT;
}
}
