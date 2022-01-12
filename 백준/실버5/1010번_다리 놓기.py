t = int(input())   # 테스트 케이스 개수

def factorial(a):  # 팩토리얼 함수
    b = 1
    for i in range(1, a+1):
        b *= i
    return b

for i in range(t):
    n, m = map(int, input().split())
    print(int(factorial(m)/(factorial(m-n) * factorial(n))))  # nCr = n!/((n-r)!*r!)