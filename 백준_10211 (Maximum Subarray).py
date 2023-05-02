
t = int(input())
result = []

for start in range(t):
    max = -9999

    n = int(input())
    num = list(map(int, input().split()))


    for i in range(len(num)):
        tmp = num[i]
        if tmp > max:
            max = tmp
        for j in range(i+1, len(num)):
            # print(j)
            tmp += num[j]
            if tmp > max:
                max = tmp

    result.append(max)


for i in result:
    print(i)
