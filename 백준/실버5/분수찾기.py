n = int(input())

before = 0
after = 0
idx = 1

flag = 1
while True:
    after += idx
    if before < n <= after:
        if flag == 1:
            print(str(idx - (n - before) + 1) + '/' + str(n - before))
            break
        else:
            print(str(n-before)+ '/'+ str(idx - (n - before) + 1))
        break
    before = after
    flag *= -1
    idx += 1