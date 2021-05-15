def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break


pinak = [9, 2, 4, 7, 1, 8, 6, 3, 3, 3, 51, 62]

insertion_sort(pinak)

print(pinak)
