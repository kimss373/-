c=int(input())  # 테스트 케이스 개수
for i in range(c):
    a = list(map(int, input().split()))  # 학생수, 점수 입력
    count = 0  # 평균 넘는 학생 수 초기값
    for j in range(1, a[0]+1):  # 모든 점수에서 평균을 넘는 학생 수 세기
        if a[j] > (sum(a)-a[0])/a[0]:
            count += 1
    print(str(format(count/a[0]*100, ".3f")) + "%")  # 소수점 3번째까지 출력
