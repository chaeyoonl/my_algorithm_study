import itertools

def pNum(number):
    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def solution(nums):
    answer = 0

    cList = list(map(list, itertools.combinations(nums, 3)))

    for i in cList:
        sumNumber = i[0] + i[1] + i[2]
        if pNum(sumNumber):
            answer += 1

    return answer
