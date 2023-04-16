from collections import deque


def bfs(graphs, V, visited):
    queue = deque([V])
    visited[V] = True

    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        V = queue.popleft()
        print(V, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i, j in graphs:
            if i == V and not visited[j]:
                queue.append(j)
                visited[j]=True



N, M, V = map(int, input().split())

graphs=[]
visited=[False]*1001

for i in range(0, M*2, 2):
    s, d = map(int, input().split())
    graphs.append([])
    graphs[i].append(s)
    graphs[i].append(d)
    graphs.append([])
    graphs[i+1].append(d)
    graphs[i+1].append(s)


graphs.sort()
bfs(graphs, V, visited)
