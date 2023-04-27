def solution(wallpaper):

    end = [0, 0]
    start = [len(wallpaper)-1, len(wallpaper[0])-1]

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < start[0]:
                    start[0] = i
                if j < start[1]:
                    start[1] = j
                if i > end[0]:
                    end[0] = i
                if j > end[1]:
                    end[1] = j

    end[0] += 1
    end[1] += 1

    return start+end

print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))