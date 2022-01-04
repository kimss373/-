n = int(input())  # 과목 개수 입력
a = list(map(int, input().split()))  # 점수 입력
a.sort()
print(sum(a)/a[-1]*100/n)  # 새로운 평균 출력