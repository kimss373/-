stack = []

def solution(n, k, cmd):

    result = ["O" for i in range(n)]
    linked_list = {i : [i-1, i+1] for i in range(1, n+1)}

    k+=1
    for c in cmd:
        if c[0] == "U":
            for i in range(int(c[2:])):
                k=linked_list[k][0]

        elif c[0] == "D":
            for i in range(int(c[2:])):
                k=linked_list[k][1]

        elif c[0] == "C":
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            result[k-1] = "X"

            if next == n+1:
                k=linked_list[k][0]
            else:
                k=linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n+1:
                linked_list[prev][1] = next
            else:
                linked_list[next][0] = prev
                linked_list[prev][1] = next

        else:
            prev, next, now = stack.pop()
            result[now-1] = "O"
            if prev == 0:
                linked_list[next][0] = now
            elif next == n+1:
                linked_list[prev][1] = now
            else:
                linked_list[next][0] = now
                linked_list[prev][1] = now

    answer = ''.join(result)
    return answer

