n = int(input())

C = []
D = []

for i in range(n):
    c,d = list(map(int,input().strip().split()))
    C.append(c)
    D.append(d)

flag = True

if max(D) == min(D) and max(D) == 1:
    print("Infinity")
else:
    if max(D) == min(D) and max(D) == 2:
        flag = False

    a = []
    b = []

    if D[0] == 1:
        a.append(0)
    else:
        b.append(0)

    currsum = 0
    prefix_sums = [0]
    for i in range(1,n):
        currsum += C[i-1]
        prefix_sums.append(currsum)
        if D[i] == 1:
            a.append(currsum)
        else:
            b.append(currsum)


    if flag:
        # a = [prefix_sums[j] for j in range(n) if D[j] == 1]
        lowest_red_point = min(a)
    highest_blue_point = max(b)

    # b = [prefix_sums[j] for j in range(n) if D[j] == 2]

    # print(C,prefix_sums)
    # print(a,b)
    # print(lowest_red_point,highest_blue_point)

    if flag and lowest_red_point <= highest_blue_point:
        print("Impossible")
    else:
        for i in range(n):
            if prefix_sums[i] == highest_blue_point:
                bp = i

        print(1899 + sum(C[bp:]))

