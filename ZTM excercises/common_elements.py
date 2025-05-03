# Given two arrays, our aim is to return 'True' if the arrays contain common elements and 'False' if the do not.
from collections import defaultdict
def common_element(array1: list, array2: list) -> bool:
    common_hash = defaultdict(int)

    for ele in array1:
        common_hash[ele] += 1

    for ele in array2:
        common_hash[ele] += 1

    for value in common_hash.values():
        if value > 1:
            return True
    return False

a = ['a', 'b', 'c', 'd']
b = ['d', 'f', 'g', 'h']
print(common_element(a, b))
