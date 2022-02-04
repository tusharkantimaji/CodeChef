# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    s = input()
    c = 0
    for i in range(n // 2):
        if s[i] != s[n-i-1]:
            c += 1
    if k < c:
        print('NO')
    # elif n%2 == 1 and c == k-1:
    #     print('YES')
    elif (k-c)%2 == 1 and n%2 == 0:
        print('NO')
    # elif (k-c)%2 == 1 and n%2 == 1:
    #     print('YES')
    else:
        print('YES')

        