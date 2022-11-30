# fibonacci sequence with recursion

# 0 1 2 3 4 5 6 7  8   9  10
# 0 1 1 2 3 5 8 13 21 34  55
# f(n) = f(n-1) + f(n-2)
# f(0) = 0
# f(1) = 1
# f(2) = 1
# f(3) = f(1) + f(2) = 1 + 1
# f(4) = f(2) + f(3) = f(1) + f(2) + f(2) = 1 + 1 + 1
# f(5) = f(3) + f(4) = f(1) + f(1) + f(2) + f(2) + f(2) = 1 + 1 + 1 + 1 +1 = 5

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))