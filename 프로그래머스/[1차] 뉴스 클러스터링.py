def solution(str1, str2):
    alpha = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    str1 = str1.upper()
    str2 = str2.upper()
    list1 = []
    list2 = []

    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if tmp[0] not in alpha or tmp[1] not in alpha:
            continue
        list1.append(tmp)

    for i in range(len(str2) - 1):
        tmp = str2[i:i + 2]
        if tmp[0] not in alpha or tmp[1] not in alpha:
            continue
        list2.append(tmp)

    list1.sort()
    list2.sort()

    idx1, idx2 = 0, 0
    cnt = 0
    while True:
        if not list1 or not list2:
            break
        if list1[idx1] == list2[idx2]:
            list1.pop(idx1)
            list2.pop(idx2)
            cnt += 1
            if idx1 == len(list1) or idx2 == len(list2):
                break
        elif list1[idx1] > list2[idx2]:
            if idx2 == len(list2)-1:
                break
            idx2 += 1
        else:
            if idx1 == len(list1)-1:
                break
            idx1 += 1

    if cnt==0:
        if list1 or list2:
            answer = 0
        else:
            answer = 65536
    else:
        answer = int(cnt/(len(list1) + len(list2) + cnt) * 65536)
    return answer
print(solution("      1 ", "e=m*c^2"))