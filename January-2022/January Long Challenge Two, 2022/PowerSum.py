for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    upper_value = 1
    while upper_value < sum(arr):
        upper_value *= 2
    s = upper_value - sum(arr) + min(arr)
    multiplier = s/min(arr)
    if multiplier == 1:
        print(0)
    else:
        print(1)
        print(1, int(multiplier))
        print(arr.index(min(arr)) + 1)

