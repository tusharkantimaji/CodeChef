# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    ans = 0
    pos = 0
    val = 1
    for i in range(n):
        if arr[pos] == val:
            ans += 1
            val += 1
        pos += 1
        val += 1

    print(ans)