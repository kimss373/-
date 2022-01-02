from string import ascii_lowercase
s=input()
alpha = {}
for i in ascii_lowercase:
    alpha[i] = 0
for j in range(len(s)):
    alpha[s[j]] += 1
for k in ascii_lowercase:
    print(alpha[k], end=" ")