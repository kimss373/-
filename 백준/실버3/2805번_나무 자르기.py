import sys
n, m = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(trees)

while start <= end:     # 이분탐색, 매개변수 탐색 start, end 중간값으로 탐색
    a = 0
    x = (end + start) // 2
    for i in trees:
        if i>x:
            a += i-x
            if a>m:     # 이미 가져갈 양을 넘었으면 계산을 종료해서 시간세이브
                break
    if a<m:
        end = x-1
    elif a>=m:
        start = x+1

print(end)