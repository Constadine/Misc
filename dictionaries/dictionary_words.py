dictionary = {
    "ιταμός": "προκλητικός, αυθάδης, αναιδής",
    "όνειδος": "ντροπή, καταισχύνη",
    "πομφόλυγες": "αερολογίες, ανοησίες"
}

print(dictionary)

dictionary["φληναφήματα"] = "ανοησίες, σαχλαμάρες"

print(dictionary)

user_key = input("Give the key: ")
user_value = input("..and it's value: ")

dictionary[user_key] = user_value

print(dictionary)
