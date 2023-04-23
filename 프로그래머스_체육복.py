def solution(n, lost, reserve):
    answer = 0
    checkLost = [False] * (n + 1)

    lost.sort()
    reserve.sort()

    # 체육복이 없는 사람과 여분의 체육복을 가진 사람이 같을 경우
    remove_list = []
    for a in reserve:
        if (a in lost):
            remove_list.append(a)

    for a in remove_list:
        lost.remove(a)
        reserve.remove(a)

    answer = n - len(lost)

    for i in lost:
        # print(i)
        for j in reserve:
            if (((i - 1) == j or (i + 1) == j) and checkLost[i] == False):
                checkLost[i] = True
                # lost.remove(i)
                reserve.remove(j)
                answer += 1
                break

    return answer
