# takes a list and returns a new list with all
# duplicates removed

# using a loop:

no_duplicates = []

duplicates_list = ["hi", "bye", "sun", "hi", "dog", "cat", "dog", "hot", "cold", "cold"]

for value in duplicates_list:
    if value in no_duplicates:
        pass
    else:
        no_duplicates.append(value)

print("duplicates_list = ", duplicates_list)
print("no_duplicates = ", no_duplicates)

# now with a set:

set_no_duplicate = set(duplicates_list)

print("set_no_duplicate = " , set_no_duplicate)
