import itertools

moum = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
munja = list(input().split())
munja.sort()
combi_list = list(itertools.combinations(munja, l))
for i in combi_list:
    m_cnt = 0
    j_cnt = 0
    for j in i:
        if j in moum:
            m_cnt += 1
        else:
            j_cnt += 1

    if m_cnt >=1 and j_cnt >=2:
        answer = ''
        for k in i:
            answer += k
        print(answer)