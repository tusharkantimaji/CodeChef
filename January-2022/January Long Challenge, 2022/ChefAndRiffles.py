def check(n, arr):
    cpy = arr
    c = 0
    while True:
        temp = []
        c += 1
        for i in range(0, n, 2):
            temp.append(arr[i])
        for i in range(1, n, 2):
            temp.append(arr[i])
        arr = temp
        if cpy == arr:
            return c

n1 = int(input())
for item in range(n1):
    n, k = list(map(int, input().split(' ')))
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    k = k % check(n, arr)
    for i in range(k):
        temp = []
        for i in range(0, n, 2):
            temp.append(arr[i])
        for i in range(1, n, 2):
            temp.append(arr[i])
        arr = temp
    for i in arr:
        print(i, end=" ")
    print()
