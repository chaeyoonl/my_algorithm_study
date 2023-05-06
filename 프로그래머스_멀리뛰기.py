def solution(n):
    answer = 0
    compareList = [0, 1, 2]
    
    if n >= 3:
        for i in range(3, n+1):
            compareList.append(compareList[i-2] + compareList[i-1])
            
    answer = compareList[n] % 1234567
    return answer
