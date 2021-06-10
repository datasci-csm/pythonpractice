# create a function to reverse the word order of a string

my_string = "Today is a sunny day and wonderfully blue sky"

def reverse_word_order(my_string):
    reversed_string = ""

    list_of_words = my_string.split()
    list_of_words.reverse()
    reversed_string = " ".join(list_of_words)

    return reversed_string


if __name__ == "__main__":
    reversed_string = reverse_word_order(my_string)
    print("my_string is ", my_string)
    print("reversed_string is ", reversed_string)
