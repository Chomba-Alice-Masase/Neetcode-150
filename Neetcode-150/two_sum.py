# BRUTE FORCE
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
                
# Hash Approach-less efficient
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_hash = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  
                total = nums[i] + nums[j]  
                sum_hash[total].append(i)
                sum_hash[total].append(j)  

        for x,y in sum_hash.items():
            if x == target:
                return y
