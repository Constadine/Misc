def sorting(l, reverse=False):
    if reverse:
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]
    else:
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]
    return l


myList = [9, 2, 4, 7, 1, 8, 6, 3]
otherList = [124, 1, 4, 52, 5, 6, 325, 6, 34, 6, 347, 8643, 64]

print(sorting(otherList))
print(sorting(otherList, reverse=True))
