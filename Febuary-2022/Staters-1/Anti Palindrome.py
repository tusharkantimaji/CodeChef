for _ in range(int(input())):
    n = int(input())
    s = input()
    if n % 2 == 1:
        print('NO')
        continue
    d = {}
    m = 1
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            m = max(m, d[i])
    # print(d)
    # print(m)
    if m > n//2:
        print('NO')
    else:
        half = n / 2
        arr = []
        for i in d:
            arr.append([i, d[i]])
        arr.sort(key=lambda x:x[1], reverse=True)
        ans1 = ''
        p1 = 0
        p2 = 0
        for i in arr:
            # print(half)
            if half > 0:
                if i[1] <= half:
                    for j in range(i[1]):
                        ans1 += (i[0])
                    half -= i[1]
                else:
                    p1 = i[0]
                    p2 = i[1]-half
                    while half > 0:
                        ans1 += (i[0])
                        half -= 1
            else:
                for j in range(i[1]):
                    ans1 += (i[0])
        # print(p1, p2)
        for i in range(int(p2)):
            ans1 += (p1)
        print('YES')
        print(ans1)


