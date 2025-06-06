from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for num in nums:
            if num == 0:
                zero = num
                nums.remove(num)
                nums.append(num)
        return nums
    
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = []
        non_zeroes = []
        for i,v in enumerate(nums):
            if v == 0:
                zeroes.append(v)
            else:
                non_zeroes.append(v)

        nums.clear()
        nums.extend(non_zeroes)
        nums.extend(zeroes)

    
nums = [0,1,0,3,12]
Solution().moveZeroes2(nums) 
print(nums) # Output: [1, 3, 12, 0, 0]  