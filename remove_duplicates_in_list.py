# takes a list and returns a new list with all
# duplicates removed

# using a loop:

duplicates_list = ["hi", "bye", "sun", "hi", "dog", "cat", "dog", "hot", "cold", "cold"]


def remove_dup(duplicates_list):

    no_duplicates = []
    
    for value in duplicates_list:
        if value in no_duplicates:
            pass
        else:
            no_duplicates.append(value)

    return no_duplicates



# now with a set:

def remove_dup_set(duplicates_list):
    
    set_no_duplicate = set(duplicates_list)
    return set_no_duplicate



if __name__ == "__main__":
    no_duplicates = remove_dup(duplicates_list)
    print("duplicates_list = ", duplicates_list)
    print("no_duplicates = ", no_duplicates)

    no_duplicates_set = remove_dup_set(duplicates_list)
    print("no_duplicate_set = " , no_duplicates_set)
