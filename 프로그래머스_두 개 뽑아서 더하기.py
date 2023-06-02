import itertools

def solution(numbers):
    answer = []

    cList = list(map(list, itertools.combinations(numbers, 2)))

    for i in cList:
        answer.append(i[0]+i[1])

    answer = list(set(answer))
    answer.sort()


    return answer
