from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram_s = defaultdict(int)
        is_anagram_t = defaultdict(int)

        for s_count in s:
            s_key = s_count
            is_anagram_s[s_key] += 1

        for t_count in t:
            t_key = t_count
            is_anagram_t[t_key] += 1

        if is_anagram_s == is_anagram_t:# remember to compare dictionaries directly.
            return True

        else:
            return False

            
        



        

