s = input()

answer = len(s)-1
for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        answer = i
        break

print(len(s) + answer)
