def binary_Search(array, x, start, finish):
    middle = (start + finish) // 2
    if start > finish:
        return -1
    else:
        if x == array[middle]:
            return middle
        elif x < array[middle]:
            return binary_Search(array, x, start, middle - 1)
        else:
            return binary_Search(array, x, middle + 1, finish)


test = [i*i for i in range(10)]

print(test)
print(binary_Search(test, 2, 0, len(test) - 1))
