import sys
n = int(sys.stdin.readline())            # 기준 수의 개수 입력
a = tuple(sys.stdin.readline().split())  # 기준 수 입력

m = int(sys.stdin.readline())            # 검사할 수의 개수 입력
b = tuple(sys.stdin.readline().split())  # 검사할 수 입력
dict_a={}
for j in b:                              # 검사할 수를 딕셔너리에 0으로 추가
    dict_a[j] = 0
for i in a:                              # 기준 수를 딕셔너리에 1로 수정 또는 추가
    dict_a[i] = 1
for k in b:                              # 검사하는 수가 기준 수에 있으면 1로 출력되고 없으면 0으로 출력됨
    print(dict_a[k])