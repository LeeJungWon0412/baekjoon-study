n = int(input())

for i in range(1, n + 1, 1):
    print("{}{}".format(" " * (n - 1), "*" * i))
    n -= 1