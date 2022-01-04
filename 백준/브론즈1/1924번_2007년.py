month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
a, b = map(int, input().split())
n = 0
for i in range(a-1):  # 월, 일을 일로 환산
    n += month[i]
m = n + b
for j in range(7):
    if m%7 == j:
        print(day[j])