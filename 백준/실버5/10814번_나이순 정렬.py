n=int(input())  # 회원 가입 수

a = []  # 회원 가입 리스트

for _ in range(n):  # 리스트에 순번과 함께 값 추가
    x, y = map(str, input().split())
    x = int(x)
    a.append([x, _,  y])

a.sort()  # 나이, 순번순 정렬

for i in a:  # 순번 제거
    i.pop(1)

for j in a:  # 출력
    print(j[0], j[1])