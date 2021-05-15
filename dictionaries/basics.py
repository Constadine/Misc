hero = {"name": "Bruce Banner", "alias": "Iron Man"}
print(hero)
# with key ["name"], changed the value from "Bruce Banner" to "Tony Stark"
hero["name"] = "Tony Stark"
# with new key ["equipment"], added a new pair of key-value
hero["equipment"] = "suite"
print(hero)

# copy:
hero1 = {"name": "Tony Stark", "alias": "Iron Man"}
hero2 = hero1.copy()

# delete:
dict_name.pop(key)

# if:
hero = {"name": "Bruce Banner", "alias": "Hulk"}
if "equipment" not in hero:
    print("No equip")

# loops:
for key in dict_name:  # keys only

for key, value in dict_name.items():  # keys and values

for key in dict_name.keys():  # no sort

for value in dict_name.values():  # me epanalipseis

    # BONUS

for key in sorted(dict_name.keys()):  # keys sorted

for key in set(dict_name.values()):  # no repeats
    # or
for value in set(dict_name.values()):
