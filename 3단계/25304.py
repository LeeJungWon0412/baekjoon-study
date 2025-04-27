x = int(input())
n = int(input())
c = 0

for i in range(1, n + 1):
    a, b = map(int, input().split())
    c += a * b

if(c == x):
    print("Yes")
else:
    print("No")