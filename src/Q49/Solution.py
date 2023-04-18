import time
from collections import Counter, defaultdict
from typing import List

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the 
original letters exactly once.
"""


class Solution:
    """
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


    Input: strs = [""]
    Output: [[""]]

    Input: strs = ["a"]
    Output: [["a"]]
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            letters = [0] * 26
            for c in string:
                letters[ord(c)-ord("a")] += 1
            groups[tuple(letters)].append(string)
        return list(groups.values())


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams(["a"]))
    print(s.groupAnagrams([""]))


