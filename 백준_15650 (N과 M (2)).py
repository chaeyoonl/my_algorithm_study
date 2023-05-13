import itertools

N, M = map(int, input().split())
tmpList = []

for i in range(1, N+1):
    tmpList.append(i)

answer = itertools.combinations(tmpList, M)

for i in answer:
    print(*i)
