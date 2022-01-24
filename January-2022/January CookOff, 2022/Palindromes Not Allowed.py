# cook your dish here
for _ in range(int(input())):
    n = int(input())
    ans = ''
    for i in range(n):
        ans += chr(97+(i%26))
    print(ans)

    