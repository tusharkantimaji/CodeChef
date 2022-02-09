# cook your dish here
for _ in range(int(input())):
    n = int(input())
    x_index = []
    y_index = []
    for i in range(n):
        x, y = map(int, input().split(' '))
        x_index.append(x)
        y_index.append(y)
    print(len(set(x_index))+len(set(y_index)))


