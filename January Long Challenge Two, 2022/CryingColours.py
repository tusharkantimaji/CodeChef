# cook your dish here
for _ in range(int(input())):
    n = int(input())
    b1 = list(map(int, input().split(' ')))
    b2 = list(map(int, input().split(' ')))
    b3 = list(map(int, input().split(' ')))
    # print(int((b1[1]+b1[2]+b2[0]+b2[2]+b3[0]+b3[1])//2))
    ans = max(b1[1]+b1[2]+b2[2], b2[0]+b3[0]+b3[1])
    print(ans)