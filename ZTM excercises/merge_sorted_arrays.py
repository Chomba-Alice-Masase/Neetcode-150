# given two sorted arrays, return a singular array that is a union of both inputs

# here's our rough approach without thinking much for efficieny
def array_merger(array1: list, array2: list) -> list:
    for int in array2: # O(n)
        array1.append(int) # O(n)

    array3 = sorted(array1) # O(nlogn)
    return array3


test_array_1 = [0, 3, 4, 41]
test_array_2 = [4, 6, 30]
print(array_merger(test_array_1,test_array_2))