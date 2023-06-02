def solution(n):
    answer = True
    visited = [False]*len(n)

    if max(n) > len(n):
        return False

    for i in n:
        if visited[i-1] == False:
            visited[i-1] = True
        else:
            answer = False
            break

    if False in visited:
        answer = False


    return answer
