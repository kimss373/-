# https://www.acmicpc.net/problem/1764
n, m = map(int, input().split())    # n:듣도 못한 사람 수, m:보도 못한 사람 수
not_listen = {}
not_seen = []
not_listen_seen = []
for _ in range(n):              # 듣도 못한 사람 dict에 적음
    not_listen[input()] = 0
for _ in range(m):              # 보도 못한 사람 list에 적음
    not_seen.append(input())
for i in not_seen:              # dict의 key에 보도못한 사람이 있으면 듣보잡리스트에 넣음
    if i in not_listen:
        not_listen_seen.append(i)
not_listen_seen.sort()          # 듣보잡 리스트 알파벳순 정렬
print(len(not_listen_seen))
for j in not_listen_seen:
    print(j)