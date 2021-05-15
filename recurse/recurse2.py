import random
import string

alphabet = string.ascii_lowercase
words = ["unfortunate", "depression", "ceremonial", "tyrant", "lights"]


def random_word(l):
    return l[random.randint(0, len(words) - 1)]


def create_discobobulated_word(word):
    for _ in range(11):
        wall = random.randint(0, len(word) - 1)
        word = word[:wall] + \
            alphabet[random.randint(0, len(alphabet) - 1)] + word[wall:]
    return word


# δε θα δουλεψει ποτέ αν δεν κραταω counter για το ποσες φορες υπαρχει το καθε γραμμα στην λεξη πριν

# def strip_recursive(init_word, disc_word, collection):
#     if disc_word == init_word:
#         return "done"
#     else:
#         print(disc_word)

#         char = input("Char: ")
#         if (char not in init_word) and (char in disc_word):
#             return strip_recursive(init_word, disc_word.strip(char), collection)
#         elif char in init_word and char in disc_word:

# def strip_while(init_word, disc_word, collection):
#     while True:
#         if init_word == disc_word:
#             return "done"
#         else:
#             for char in collection:
#                 print(char, init_word, disc_word)
#                 if char not in init_word and char in disc_word:  
#                     print("in first if")
#                     disc_word = disc_word.strip(char)    # αυτο γιατι δε δουλευει ομως?
#                     print(disc_word) 
#                 elif char in init_word and char in disc_word:
#                     print("Char exists in initial word.")


def main():
    init_word = random_word(words)
    disc_word = create_discobobulated_word(init_word)
    print(strip_while(init_word, disc_word, alphabet))


main()
