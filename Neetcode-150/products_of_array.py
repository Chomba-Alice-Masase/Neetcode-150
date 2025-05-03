from functools import reduce
from operator import mul
class Solution:
    # Brute Force.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            temp = list(nums)
            temp.remove(num)
            product = reduce(mul, temp)
            result.append(product)
           
        return result

        
  

test_array = [-1,0,1,2,3]
solution = Solution()
print(solution.productExceptSelf(test_array))