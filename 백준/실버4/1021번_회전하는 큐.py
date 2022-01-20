# https://www.acmicpc.net/problem/1021
n, m = map(int, input().split())
a = [i for i in range(1, n+1)]  # 큐 생성
b = list(map(int, input().split()))     # 뽑아내고자 하는 수
count = 0
for j in b:
    index = a.index(j)  # 뽑아내고자 하는 수의 index
    if index <= len(a)//2:  # index가 큐의 길이의 반보다 작거나 같으면 인덱스만큼 2번째 연산 반복
        for _ in range(index):
            a.append(a.pop(0))
            count += 1

    else:                   # index가 큐의 길이의 반보다 크면 인덱스만큼 3번째 연산 반복
        for _ in range(len(a)-index):
            a.insert(0, a.pop())
            count += 1
    a.pop(0)    # 1번째 연산 수행
print(count)