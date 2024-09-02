word = input()

idx = 0

tmp = ''
while idx < len(word):
    if word[idx] == '<':
        if tmp != '':
            tmpList = list(tmp)
            tmpList.reverse()
            tmp = ''.join(tmpList)
            print(tmp, end="")
            tmp = ''
        while word[idx] != '>':
            tmp += word[idx]
            idx += 1
        tmp += '>'
        idx += 1
        print(tmp, end="")
        tmp = ''
        continue

    if word[idx] != " ":
        tmp += word[idx]
        idx += 1
    else:
        tmpList = list(tmp)
        tmpList.reverse()
        tmp = ''.join(tmpList)
        print(tmp, end=" ")
        idx += 1
        tmp = ''

if tmp != '':
    tmpList = list(tmp)
    tmpList.reverse()
    tmp = ''.join(tmpList)
    print(tmp, end="")
    tmp = ''
