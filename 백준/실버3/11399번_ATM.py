n = int(input())
a = list(map(int, input().split()))     # 걸리는 시간을 리스트로 받음
a.sort()    # 리스트 오름차순 정렬

min_sum = 0
for i in range(n):
    min_sum += sum(a[0:i+1])    # 각 사람 마다 걸리는 시간을 모두 더한 값의 최소값
print(min_sum)