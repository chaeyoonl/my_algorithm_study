def solution(s):
    answer = -1
    tempStack = []

    for i, str in enumerate(s):
        if (len(tempStack) > 0 and str == tempStack[-1]):
            tempStack.pop()
        else:
            tempStack.append(str)
        if len(tempStack) > 0:
            answer = 0
        else:
            answer = 1

    return answer
