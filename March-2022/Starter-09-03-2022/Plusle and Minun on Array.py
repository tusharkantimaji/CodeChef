for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    for i in range(n):
        if i % 2 == 0:
            arr1.append(abs(arr[i]))
        else:
            arr2.append(abs(arr[i]))
    s1 = sum(arr1) - min(arr1)
    s2 = sum(arr2) - max(arr2)
    ans1 = (s1-s2+max(arr2)-min(arr1))
    ans2 = sum(arr1) - sum(arr2)
    print(max(ans1, ans2))