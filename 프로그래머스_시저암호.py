def solution(s, n):
    answer = ''
    
    for i in s:
        if i == " ":
            answer += " "
            continue
            
        if (i.islower()):
            if (ord(i)+n > ord("z")):
                tmp = ord(i)+n - ord("z") - 1
                answer += chr(ord("a")+tmp)
                continue
        else:
            if (ord(i)+n > ord("Z")):
                tmp = ord(i)+n - ord("Z") - 1
                answer += chr(ord("A")+tmp)
                continue
            
        answer += chr(ord(i)+n)
    
    
    
    return answer
