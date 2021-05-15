def binary_Search(array, x):
    def bs(array, x, start, finish):
        middle = (start + finish) // 2
        if start > finish:
            return -1
        else:
            if x == array[middle]:
                return middle
            elif x < array[middle]:
                return bs(array, x, start, middle - 1)
            else:
                return bs(array, x, middle + 1, finish)

    return bs(array, x, 0, len(array)-1)


test = [i*i for i in range(10)]

print(test)
print(binary_Search(test, 4))
