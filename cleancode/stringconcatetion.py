# .join() !
import sys

list_of_strings = ["Hello", "my", "friend"]

# BAD:

my_bad_string = ""
for i in list_of_strings:
    my_bad_string += i + " "

print(my_bad_string)


# GOOD:
my_good_string = " ".join(list_of_strings)

print(my_good_string)
