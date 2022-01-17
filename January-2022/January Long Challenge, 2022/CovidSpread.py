

for _ in range(int(input())):
    n, k = list(map(int, input().split(' ')))
    c = 1
    for i in range(1, k+1):
        if i <= 10:
            c *= 2
        else:
            c *= 3
        if c >= n:
            c = n
            break
    print(c)

    