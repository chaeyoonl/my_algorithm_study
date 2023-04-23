from collections import deque



def bfs(begin, target, words):
    queue = deque([begin])
    tmp_answer = 0

    while (queue):
        start = queue.popleft()
        words.sort(key=lambda x: sum([1 for i in range(len(x)) if x[i] != target[i]]))
        for i in words:
            if sum([1 for a, b in zip(start, i) if a != b]) == 1:
                queue.append(i)
                words.remove(i)
                tmp_answer+=1
                if (i == target):
                    return tmp_answer
                break
    return tmp_answer

def solution(begin, target, words):
    answer = 0

    if (target in words):
        answer = bfs(begin, target, words)

    return answer


print(solution("aba", "agc", ["aaa", "aac", "agc"]))  # 기댓값: 3
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "dot", "hot"]))  # 기댓값: 4



