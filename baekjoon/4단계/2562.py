a = []
max = 0
n = 0

for i in range(9):
    a.append(int(input()))

for i in range(9):
    if a[i] > max:
        max = a[i]
        n = i + 1

print(max)
print(n)