# https://www.acmicpc.net/problem/9012

t = int(input())  # 테스트케이스 수

for i in range(t):  # 테스트 케이스만큼 반복
    stringg = list(map(str, input()))   # 문자열 리스트에 하나씩 입력
    while True:
        a = 0                           # 스위치(a가 안바뀌면 while문 종료)
        for i in range(len(stringg)-1):
            if stringg[i] == "(" and stringg[i+1] == ")":  # (와 )가 연속으로 있으면 둘 다 제거
                stringg.pop(i)
                stringg.pop(i)
                a = 1                   # 제거되면 while문 재실행
                break


        if a == 0:
            break
    if stringg == []:
        print("YES")
    else:
        print("NO")