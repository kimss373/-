n = int(input())  # 배달해야하는 설탕의 무게
a=[]
for i in range(0, n//5+1):  # n에서 5씩 빼가며 3으로 나눠지는 경우 모두 수집
    if (n - 5*i)%3 == 0:
        a.append(i + ((n-5*i)//3))
a.sort()  #모든 경우의수 오름차순배열
if a==[]:  #출력
    print("-1")
else:
    print(a[0])