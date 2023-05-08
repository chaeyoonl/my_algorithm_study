def solution(s):
    answer = True
    countP = 0
    countY = 0
    
    for i in s:
        if i == "p" or i == "P":
            countP += 1
        if i == "y" or i == "Y":
            countY += 1
            
    if countP != countY:
        answer = False
    

    return answer
