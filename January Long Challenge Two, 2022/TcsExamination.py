for _ in range(int(input())):
    marks_1 = list(map(int, input().split(' ')))
    marks_2 = list(map(int, input().split(' ')))
    if sum(marks_1) > sum(marks_2):
        print("DRAGON")
    elif sum(marks_1) < sum(marks_2):
        print('SLOTH')
    elif marks_1[0] > marks_2[0]:
        print("DRAGON")
    elif marks_1[0] < marks_2[0]:
        print('SLOTH')
    elif marks_1[1] > marks_2[1]:
        print("DRAGON")
    elif marks_1[1] < marks_2[1]:
        print('SLOTH')
    else:
        print("TIE")