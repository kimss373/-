n, m = map(int, input().split())

def two_cnt(n):
    cnt = 0
    while n!=0:
        n = n//2
        cnt += n
    return cnt

def five_cnt(n):
    cnt = 0
    while n!=0:
        n = n//5
        cnt += n
    return cnt

print(min(two_cnt(n)-two_cnt(n-m)-two_cnt(m), five_cnt(n)-five_cnt(n-m)-five_cnt(m)))