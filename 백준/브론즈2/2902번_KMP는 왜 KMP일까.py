a=list(map(str, input().split("-"))) # 단어입력

for i in range(len(a)): #짧은 형태 이름 출력
    print(a[i][0], end="")