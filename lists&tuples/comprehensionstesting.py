old_list = [1, 2, 3]


# for element in old_list:
#     new_list.append(element)


# new_list = [element for element in old_list if element < 3]

new_list = [element if element < 2 else "No" for element in old_list]

print(new_list)