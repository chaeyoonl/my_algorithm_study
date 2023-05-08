def solution(s):
    answer = ''
    strTmp=[]
    
    for i in s:
        strTmp.append(ord(i))
        
    strTmp=sorted(strTmp, key=lambda x:x, reverse=True)
    
    for i in strTmp:
        answer+=chr(i)
        
    return answer
