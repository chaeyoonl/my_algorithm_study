import itertools


def isprime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num + 1):
        if i != 1 and i != num and num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    tmp = []
    notDouble = []

    for i in range(len(numbers)):
        tmp.append(list(map(''.join, itertools.permutations(numbers, i + 1))))

    tmp = list(set(sum(tmp, [])))

    for num in tmp:
        if isprime(int(num)) and not int(num) in notDouble:
            notDouble.append(int(num))
            answer += 1

    return answer
