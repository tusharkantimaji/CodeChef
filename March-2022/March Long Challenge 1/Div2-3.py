# cook your dish here
for _ in range(int(input())):
    s = input()
    if len(s) < 2 or len(set(s)) == 1:
        print(-1)
        continue
    max_len = 0
    l = len(s)
    arr = [s[0], s[-1]]
    count = 0
    for i in range(1, l-1):
        if s[i] not in arr:
            count += 1
        else:
            max_len = max(max_len, count)
            count = 0
    max_len = max(max_len, count)
    if max_len == 0:
        print(-1)
    else:
        print(max_len)