# We will reverse string 'Hi, my name is Andrew!'

def reverse_string_one(msg: str) -> str:
    new_msg = '' # O(1)
    for counter in range(len(msg)-1, -1, -1):
        new_msg += msg[counter] # O(k) as we are creating a new list each time we concatenate a character

    return new_msg # O(1)

# This solution has a time complexity of O(n^2) not efficient

# This solution was provided my gemini.
def reverse_string_efficient(msg: str) -> str:
    list_msg = list(msg) # O(n)
    list_msg.reverse()   # O(n)
    return "".join(list_msg) # O(n)

test = "Hi, my name is Andrew"
print(reverse_string_one(test))