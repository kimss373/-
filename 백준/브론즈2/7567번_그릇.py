a=input() #그릇 입력
count = 10 #첫 그릇 높이 초기값
for i in range(1, len(a)): # 2~n번째 높이 더하기
    if a[i] == a[i-1]:
        count += 5

    else:
        count += 10

print(count) #출력