from collections import defaultdict
from typing import List

def first_recurring_character(nums: List) -> int:
    num_hash = defaultdict(int)

    for num in nums:
        num_hash[num] +=1

    for key, value in num_hash.items():
        if value > 1:
            return key

def first_recurring_character2(nums: List) -> int:
    num_hash = defaultdict(int)

    for num in nums:
        num_hash[num] +=1
        if num_hash[num] > 1:
            return num

   
test = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# expected result is 2

test2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# expected result is 1

test3 = [2, 3, 4, 5]

# expected result is undefined

function_test = first_recurring_character2(test)
function_test2 = first_recurring_character2(test2)
function_test3 = first_recurring_character2(test3)
print(f"Test 1: {function_test} - Expected: 2")
print(f"Test 2: {function_test2} - Expected: 1")
print(f"Test 3: {function_test3} - Expected: undefined")