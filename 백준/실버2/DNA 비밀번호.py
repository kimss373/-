s, p = map(int, input().split())
dna = input()
arr = list(map(int, input().split()))

start = 0
end = p-1

cntDict = {'A':0, 'C':0, 'G':0, 'T':0}
for i in range(0, p):
    cntDict[dna[i]] += 1

answer = 0
while True:
    if cntDict['A'] >= arr[0] and cntDict['C'] >= arr[1] and cntDict['G'] >= arr[2] and cntDict['T'] >= arr[3]:
        answer += 1

    if end == s-1:
        break

    cntDict[dna[start]] -= 1
    cntDict[dna[end+1]] += 1
    start += 1
    end += 1

print(answer)