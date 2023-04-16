from collections import deque

def solution(maps):
    answer = 0
    #서, 북, 동, 남
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    def dfs(x, y):
    
        queue=deque()
        queue.append((x,y))
        # print(queue)

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                tx = x+dx[i]
                ty = y+dy[i]
                if (tx>=0 and tx<=len(maps)-1 and ty>=0 and ty<=len(maps[0])-1):
                    if (maps[tx][ty] == 1):
                        maps[tx][ty]=maps[x][y]+1
                        queue.append((tx,ty))
                        

        if (maps[len(maps)-1][len(maps[0])-1] == 1):
            return -1
        else:
            return maps[len(maps)-1][len(maps[0])-1]
        
    
        
    answer = dfs(0, 0)
    
    
    return answer
