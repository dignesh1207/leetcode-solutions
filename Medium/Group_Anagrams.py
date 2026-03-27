# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.  there are only 26 unique letters at most 

# time: O(n*k), space: O(n)

# ord -> given a character, return it's ASCII value 

from collections import defaultdict

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list) # O(n) -> Space

        for word in strs: # O(n) -> Time
            key = counter(word) # O(m) -> Time
            groups[key].append(word) 
                 
        return list(groups.values())  
    
def counter( word: List[str]) -> tuple[int]:
        result = [0]*26 # O(26) = O(1) -> space

        for ch in word:   # O(m) -> time, m is len(word)
            result[ord(ch)-ord('a')] += 1
        
        return tuple(result)



