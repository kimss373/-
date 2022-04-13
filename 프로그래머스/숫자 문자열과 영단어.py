def solution(s):
    answer = ''
    cursur = 0
    while cursur<=len(s)-1:
        if s[cursur] == 'z':
            answer += '0'
            cursur += 4
        elif s[cursur] == 'o':
            answer += '1'
            cursur += 3
        elif s[cursur] == 't':
            if s[cursur+1] =='w':
                answer += '2'
                cursur += 3
            else:
                answer += '3'
                cursur += 5
        elif s[cursur] == 'f':
            if s[cursur+1] == 'o':
                answer += '4'
                cursur += 4
            else:
                answer += '5'
                cursur += 4
        elif s[cursur] == 's':
            if s[cursur+1] == 'i':
                answer+='6'
                cursur+=3
            else:
                answer+='7'
                cursur+=5
        elif s[cursur]=='e':
            answer += '8'
            cursur += 5
        elif s[cursur] == 'n':
            answer += '9'
            cursur += 4
        else:
            answer += s[cursur]
            cursur+=1


    return int(answer)