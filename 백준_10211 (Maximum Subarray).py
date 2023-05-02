
t = int(input())
result = []

for start in range(t):
    n = int(input())
    num = list(map(int, input().split()))


    for i in range(1, len(num)):
        if num[i-1] > 0:
            num[i] += num[i-1]

    result.append(max(num))


for i in result:
    print(i)
