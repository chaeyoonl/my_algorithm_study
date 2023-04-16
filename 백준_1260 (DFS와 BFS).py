from collections import deque

def dfs(graphs, V, visited):
    #현재 노드를 방문 처리
    visited[V]=True
    print(V, end=' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i, j in graphs:
        if i == V and not visited[j]:
            dfs(graphs, j, visited)

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

# 값을 입력받음
for i in range(0, M*2, 2):
    s, d = map(int, input().split())
    graphs.append([])
    graphs[i].append(s)
    graphs[i].append(d)
    graphs.append([])
    graphs[i+1].append(d)
    graphs[i+1].append(s)


graphs.sort()
# for i in graphs:
#     print(i)


dfs(graphs, V, visited)
print(sep='\n')
visited=[False]*1001
bfs(graphs, V, visited)



