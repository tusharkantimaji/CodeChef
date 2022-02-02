for _ in range(int(input())):
    x, y = map(int, input().split(' '))
    ans = x + y
    if x == y:
        ans -= 1
    print(ans)