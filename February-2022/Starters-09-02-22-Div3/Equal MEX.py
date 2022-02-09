for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    nums = [0] * (2*n)
    for i in arr:
        nums[i] += 1
    for i in nums:
        if i == 0:
            print('YES')
            break
        elif i < 2:
            print('NO')
            break
    else:
        print('YES')

        