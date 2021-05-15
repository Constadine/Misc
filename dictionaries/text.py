string = "This study is unique in its nature and was hard to develop. Bare feelings had to be handled gently and presented in a fluid way. Most definitely, \
    it will gush out most of the fog surrounding the occasion. Future studies could be steered towards the transmitter’s heart in order to attain a complete \
    portrait of the story. It can be concluded that his heart is not ruled by a solitary King, but a Queen’s influence is waving it’s strings. \
    A mysterious Queen, yet righteous and unique. The incarnation of anangel, that no man deserves, yet everyone needs."

my_list = list(string)

dictionary = {}

for char in my_list:
    if char not in dictionary:
        dictionary[char] = 1
    else:
        dictionary[char] += 1

maximum = max(list(dictionary.values()))

for key, value in dictionary.items():
    if value == maximum:
        print(f"This is the max: '{key}'")
