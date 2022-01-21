n = int(input())
students =[]
for i in range(n):
    a, b, c, d = map(str, input().split())
    students.append((a, int(b), int(c), int(d)))
students.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])