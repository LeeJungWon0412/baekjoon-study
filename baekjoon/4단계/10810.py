n, m = map(int, input().split())
b = []

for i in range(n):
    b.append(0)

for a in range(m):
    i, j, k = map(int, input().split())
    for c in range(i - 1, j):
        b[c] = k

for d in range(n):
    print(b[d], end = " ")