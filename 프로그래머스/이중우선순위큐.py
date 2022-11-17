import heapq
def solution(operations):
    tmp = []
    tmp1 = []
    heapq.heapify(tmp)
    heapq.heapify(tmp1)
    for i in operations:
        if i[0] == "I":
            heapq.heappush(tmp, int(i[2:]))
            heapq.heappush(tmp1, -int(i[2:]))
        else:

            if not tmp:
                continue

            if i[2] == "-":
                x = heapq.heappop(tmp)
                tmp1.remove(-x)
            else:
                x = heapq.heappop(tmp1)
                tmp.remove(-x)

    if not tmp:
        answer = [0, 0]
    else:
        answer = [-heapq.heappop(tmp1), heapq.heappop(tmp)]
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I 16", "I 16", "D 1", "D 1"]))