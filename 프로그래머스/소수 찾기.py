from itertools import permutations

def solution(numbers):
    permu = []
    result = []
    for i in range(2, len(numbers)+1):
        a = list(permutations(numbers, i))
        permu += a
    permu = list(set(permu))
    permu += list(numbers)
    for i in permu:
        x = 0
        if i == '1' or i=='0':
            continue

        elif len(i) == 1:
            num = int(i)
            tmp = int(int(i)**0.5)
            for j in range(2, tmp+1):
                if num%j == 0:
                    x = 1
                    break

        else:
            num = ''
            for k in i:
                num += k
            num = int(num)
            if num==1 or num==0:
                continue
            tmp = int(num**0.5)
            for l in range(2, tmp+1):
                if num % l == 0:
                    x = 1
                    break


        if x==0 and num not in result:
            result.append(num)
    return len(result)

print(solution('013'))