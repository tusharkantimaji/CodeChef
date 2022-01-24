# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    arr.sort()
    print(sum(arr[:n-1])/(n-1)+arr[-1])
