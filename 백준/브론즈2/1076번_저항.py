color = {"black" : ("0", 1),
         "brown" : ("1", 10),
         "red"   : ("2", 100),
         "orange": ("3", 1000),
         "yellow": ("4", 10000),
         "green" : ("5", 100000),
         "blue"  : ("6", 1000000),
         "violet": ("7", 10000000),
         "grey"  : ("8", 100000000),
         "white" : ("9", 1000000000)} # 색과 그에따른 값
# 입력
first = input()
second = input()
third = input()

#출력
a=0
print(int(color[first][0] + color[second][0])*color[third][1])