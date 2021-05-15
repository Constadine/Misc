edres = [55, 28, 20, 40, 14, 16]


n = int(input(f"{edres}\nΟ πίνακας περιέχει τις έδρες {len(edres)} κομμάτων που φαίνονται παραπάνω. Πόσων το μέσο όρο θες: "))
temp = edres[:(n)]
# print(edres)

Sum = 0
for i in range(len(temp)):
    Sum += temp[i]
    # print(Sum,i,n)

print(f"Ο μέσος όρων των {str(n)} κομμάτων είναι: " + str(Sum/n))

