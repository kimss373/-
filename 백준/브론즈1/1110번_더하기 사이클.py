n = int(input())
a = n
cycle = 0 #n사이클
while True: # 사이클 굴리기
    a = (a%10)*10 + (a//10 + a%10)%10
    cycle += 1
    if a == n:
        break
print(cycle)