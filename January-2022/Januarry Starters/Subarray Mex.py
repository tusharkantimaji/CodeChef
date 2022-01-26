for _ in range(int(input())):
    n, k, x = list(map(int, input().split(' ')))
    if k < x:
        print(-1)
        continue
    p = 0
    while n >= 0:
        print(p %x, end=" ")
        p+=1
        n -= 1
    print()