def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    def dfs(i, visited):
        for j in range(n):
            if (i != j and computers[i][j] == 1 and computers[j][i] == 1 and visited[j] == False):
                visited[j] = True

                dfs(j, visited)
                    
    
    for i in range(n):
        if (visited[i] == False):
            visited[i] = True
            dfs(i, visited)
            answer += 1
    
    
    return answer
