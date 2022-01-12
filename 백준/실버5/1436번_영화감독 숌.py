n=int(input())  # 몇 번째 영화?

number = 666
count = 0

while True:
    if "666" in str(number):  # 666이 있는 숫자마다 카운트 +1
        count += 1

    if count == n:  # 666이 있는 n번째 숫자에 break
        break

    number += 1
print(number)