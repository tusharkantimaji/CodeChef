for _ in range(int(input())):
    n, x = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    arr.sort(reverse=True)
    c = 0
    s = 0
    for i in arr:
        c += 1
        s += i
        if s >= x:
            print(c)
            break
    else:
        print(-1)
