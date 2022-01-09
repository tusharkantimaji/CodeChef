
n = int(input())
for i in range(n):
    p = input().split(' ')
    if int(p[0])**2/int(p[2])**3 == int(p[1])**2/int(p[3])**3:
        print('YES')
    else:
        print('NO')

