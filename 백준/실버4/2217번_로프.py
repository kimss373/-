n=int(input())  # 로프 개수
rope = []   # 로프 길이 배열
diction = {}    # 로프 길이마다의 개수
for _ in range(n):
    rope.append(int(input()))

rope.sort()

for i in rope:
    if i in diction:
        diction[i] = diction[i] +1
    else:
        diction[i] = 1
sumarr = []
length = len(rope)
for j in diction:
    sumarr.append(j*length)
    length = length - diction[j]
sumarr.sort()
print(sumarr[-1])