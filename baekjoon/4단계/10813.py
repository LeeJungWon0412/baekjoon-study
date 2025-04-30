n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(i + 1)

for a in range(m):
    i, j = map(int, input().split())
    k = arr[i - 1]
    arr[i - 1] = arr[j - 1]
    arr[j - 1] = k

for i in range(n):
    print(arr[i], end = " ")