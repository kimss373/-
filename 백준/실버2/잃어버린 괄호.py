sick = input()

idx = 0
tmp = ''
answer = 0
isMinus = False
while idx < len(sick):
    if '0' <= sick[idx] <= '9':
        tmp += sick[idx]
        idx += 1
        continue


    if isMinus:
        answer -= int(tmp)
    else:
        answer += int(tmp)
    tmp = ''
    if sick[idx] == '-':
        isMinus = True
    idx += 1

if isMinus:
    answer -= int(tmp)
else:
    answer += int(tmp)
print(answer)
