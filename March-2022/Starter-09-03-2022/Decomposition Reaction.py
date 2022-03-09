n, m = map(int, input().split())
q = list(map(int, input().split()))
arr = []
for i in range(m):
    c, x = map(int, input().split())
    wc = list(map(int, input().split()))
    arr.append([[c, x], wc])
for i in arr:
    for j in range(0, len(i[1]), 2):
        q[i[1][j+1]-1] += (i[1][j]) * q[i[0][0]-1]
    q[i[0][0]-1] = 0
for i in q:
    print(i%1000000007)
