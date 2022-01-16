# https://www.acmicpc.net/problem/1002 터렛

t = int(input())   # 테스트 케이스 수

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:  # 시야(원)가 완전 겹칠 경우
        print(-1)

    elif ((x1-x2)**2 + (y1-y2)**2)**0.5 == r1+r2 or (r1-r2)**2 == (x1-x2)**2 + (y1-y2)**2:  # 시야(원)가 바깥 또는 안에서 하나만 겹칠 경우
        print(1)

    elif (x1-x2)**2 + (y1-y2)**2 < (r1-r2)**2:  # 시야(원)가 안쪽에서 안겹칠 경우
        print(0)

    elif ((x1-x2)**2 + (y1-y2)**2)**0.5 > r1+r2:  # 시야(원)가 바깥쪽에서 안겹칠 경우
        print(0)

    else:                                        # 나머지는 교점 2개
        print(2)
