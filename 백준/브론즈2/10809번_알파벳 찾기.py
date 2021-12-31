s = list(map(str, input()))
from string import ascii_lowercase
alphabet_dict = {}
for i in ascii_lowercase:
    alphabet_dict[i] = -1

for j in range(len(s)):
    if alphabet_dict[s[j]] != -1:
        pass
    else:
        alphabet_dict[s[j]] = alphabet_dict[s[j]] + j + 1
for key in alphabet_dict.keys():
    print(alphabet_dict[key], end=" ")