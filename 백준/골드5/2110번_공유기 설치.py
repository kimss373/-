import sys, bisect
input = sys.stdin.readline
op_list = list(map(int, input().split()))
coord_list = sorted([int(input()) for i in range(op_list[0])])

start = 1
end = max(coord_list) - min(coord_list)

while True:
    median = (start + end) // 2

    starter = coord_list[0]
    starter_index = 0
    router_count = 0
    while starter_index<len(coord_list):
        router_count += 1
        starter_index = bisect.bisect_left(coord_list, coord_list[starter_index]+median)

    if router_count < op_list[1]:
        end = median -1
    elif router_count >= op_list[1]:
        start = median +1
    if median == end:
        print(median)
        break