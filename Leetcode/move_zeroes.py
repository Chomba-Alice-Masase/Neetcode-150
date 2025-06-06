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
    
nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))  # Output: [1, 3, 12, 0, 0]  