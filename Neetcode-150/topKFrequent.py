a = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
k = 2
frequent_list = []

# Get unique values from the list
unique_values = list(set(a))

# Sort the unique values in descending order
unique_values.sort(reverse=True)

# Add the top k most frequent unique values to the frequent_list
for value in unique_values:
    frequent_list.append(value)
    k -= 1
    if k == 0:
        break

print(frequent_list)
