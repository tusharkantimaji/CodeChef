# cook your dish here
for _ in range(int(input())):
    val = int(input())
    s = input()
    c1 = 0
    c2 = 0
    d = 0
    for i in s:
        if i == 'C':
            c1 += 1
        elif i == 'N':
            c2 += 1
        else:
            d += 1
    c1_points = c1*2 + d
    c2_points = c2*2 + d
    if c1_points > c2_points:
        print(60*val)
    elif c1_points < c2_points:
        print(40*val)
    else:
        print(55*val)

        