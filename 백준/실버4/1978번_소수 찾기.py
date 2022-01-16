n = int(input())  # n을 입력받음

a = list(map(int, input().split()))  # 검사하려는 숫자 n개를 입력받음

count = 0  # 소수의 개수 초기화

for i in a:  # 소수인지 확인
    b=2
    c = [1]
    if i == 1:
        continue

    while i>b:
        if i%b == 0:
            c = [2]
            break
        b += 1
    if c == [1]:
        count += 1

print(count)