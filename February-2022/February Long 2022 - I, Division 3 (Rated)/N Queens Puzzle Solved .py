# cook your dish here
for _ in range(int(input())):
    n = int(input())
    d = 0.143 * n
    ans = 1
    for i in range(n):
        ans *= d
    if ans - int(ans) < 0.5:
        print(int(ans))
    else:
        print(int(ans)+1)

        