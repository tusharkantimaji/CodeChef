for _ in range(int(input())):
    n = int(input())
    x = 0
    while(n%2==0):
        n /= 2
        x += 1
    print(x)
