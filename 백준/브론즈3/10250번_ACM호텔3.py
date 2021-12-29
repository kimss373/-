testcase = int(input())  # 테스트 케이스 수

for tc in range(testcase):
    h, w, n = map(int, input().split())  # hxw 크기의 호텔, n번째 손님
    count = 0

    for i in range(1,w+1):
        for j in range(1,h+1):
            count += 1
            if count == n:
                if i < 10:
                    answer = str(j) + "0" + str(i)
                else:
                    answer = str(j) + str(i)

    print(answer)