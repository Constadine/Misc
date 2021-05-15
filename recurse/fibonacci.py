def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n):
    fib = [0, 1]

    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]


for i in range(100):
    print(fibonacci2(i))

# for i in range(100):
#     print(f"fibonacci({i})={fibonacci(i)}")
