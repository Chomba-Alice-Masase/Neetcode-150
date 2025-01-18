#Code Bagel solution
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_hash[sorted_s].append(s)
        
        for value in anagram_hash.values():
            result.append(value)

        return result
        