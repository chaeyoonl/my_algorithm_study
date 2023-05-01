import itertools

n, m = map(int, input().split())
nList = []
for i in range(1, n+1):
    nList.append(i)

answerList = list(map(list, itertools.permutations(nList, m)))

for answer in answerList:
    print(*answer)

