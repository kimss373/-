def solution(n):
    answer = ''
    while n>=1:
        if n%3!=0:
            answer += str(n%3)
            n//=3
        else:
            answer += "4"
            n=n//3-1
    reversed_answer = "".join(reversed(answer))
    return reversed_answer