# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split(' '))
    if x % 3 == 0:
        correct = x // 3
    else:
        correct = x // 3 + 1
    incorrecet = correct*3 - x
    # print(correct, incorrecet)
    if correct + incorrecet <= n:
        print('YES')
        print(correct, incorrecet, n - correct - incorrecet)
    else:
        print('NO')
