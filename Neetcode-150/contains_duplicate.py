from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value_map = defaultdict(int) # using the defaultdict int 

        for num in nums: # in this loop, we are initializing the dictionary key-value pairs
            key_num = num # assigning the value of num to key_num
            value_map[key_num] += 1 # incrementing the value of the key by one based on each instance

        for value_count in value_map.values(): # iterating through the list of values
            if value_count > 1: # a value greater than 1 indicates a duplicate.
                return True
        else:
            return False