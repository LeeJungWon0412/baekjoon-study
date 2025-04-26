h, m = map(int, input().split())

if(m - 45 >= 0):
    m = m - 45
    print(h, m)
elif(m - 45 < 0):
    if(h - 1 < 0):
        h = 24 - 1
    else:
        h = h - 1
    m = m + 15
    print(h, m)