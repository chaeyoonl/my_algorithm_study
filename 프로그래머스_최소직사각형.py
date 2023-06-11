def solution(sizes):
    answer = 0
    wallet = [0]*2

    for i in sizes:
        if wallet[0] < max(i):
            wallet[0] = max(i)
        if wallet[1] < min(i):
            wallet[1] = min(i)

    answer = wallet[0]*wallet[1]

    return answer
