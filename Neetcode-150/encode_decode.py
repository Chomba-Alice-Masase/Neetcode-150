# ChatGPT Solution
class Solution:
    def encode(self, strs: list[str]) -> str:  # Combine the list into a single string using @4 as a delimiter
        # Use the `join` method for cleaner code
        encoded_string = '@4'.join(strs) + '@4'  # Add a trailing delimiter to mark the end
        print("Encoded String:", encoded_string)
        return encoded_string

    def decode(self, s: str) -> list[str]:  # Split the encoded string back into a list of strings
        # Use `split` to separate by the delimiter `@4`
        words_list = s.split('@4')[:-1]  # Remove the trailing empty string caused by the last delimiter
        print("Decoded List:", words_list)
        return words_list


# Example Usage
solution = Solution()
test_list = ["neet code", "I", "love", "you so much"]
test_string = solution.encode(test_list)
test_decode = solution.decode(test_string)

# Output
print(test_decode)

# My Solution. A little dumb, if you ask me.
class Solution:
    # string_dict = defaultdict(list)
    def encode(self, strs: List[str]) -> str: # This section lets us merge into a single string
        encoded_string = ""
        for wrd in strs:
            encoded_string = encoded_string + wrd + '-'
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]: # This is where we break the string back into a list
        word = ""
        words_list = []
        for letter in s:
            if letter != '-':
                word += letter
            
            if letter == '-' :
                words_list.append(word)
                word = ""

        return words_list



