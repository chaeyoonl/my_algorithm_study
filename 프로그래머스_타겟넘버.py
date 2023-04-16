def solution(numbers, target):
    answer = 0

    def dfs(i, N, num, target, answer, numbers):
        if (i == N ):
            if (num == target):
                answer += 1
        else:
            data1 = num + numbers[i]
            answer = dfs( i+1, N, data1, target, answer, numbers)
            data2 = num - numbers[i]
            answer = dfs( i+1, N, data2, target, answer, numbers)


        return answer

    N = len(numbers)
    num = 0

    answer = dfs(0, N, num, target, answer, numbers)

    return answer
