import sys
sys.setrecursionlimit(10**6)


dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
answer = []


def dfs(y, x, visited, mapList):

    for i in range(8):
        # 상, 하, 좌, 우 확인
        if y + dy[i] >= 0 and y + dy[i] < len(mapList) and x + dx[i] >= 0 and x + dx[i] < len(mapList[0]):
            if mapList[y + dy[i]][x + dx[i]] == 1 and visited[y + dy[i]][x + dx[i]] == False:
                visited[y + dy[i]][x + dx[i]] = True
                dfs(y + dy[i], x + dx[i], visited, mapList)


while 1:
    tmpAnswer = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    visited = [[False]*w for _ in range(h)]
    mapList = [[0]*w for _ in range(h)]

    # 값을 입력
    for y in range(h):
        row = list(map(int, input().split()))
        for x in range(w):
            mapList[y][x] = row[x]

    # dfs 탐색 시작
    for y in range(h):
        for x in range(w):
            if mapList[y][x] == 1 and visited[y][x] == False:
                visited[y][x] == True
                tmpAnswer += 1
                dfs(y, x, visited, mapList)

    answer.append(tmpAnswer)


for i in answer:
    print(i)



