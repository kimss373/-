from string import ascii_lowercase
from string import ascii_uppercase
a = input()
dict_up = {}
for i in ascii_uppercase:
    dict_up[i] = 0
for j in a:
    if j in ascii_uppercase:
        dict_up[j] = dict_up[j] + 1
    elif j in ascii_lowercase:
        for k in range(len(ascii_lowercase)):
            if j == ascii_lowercase[k]:
                dict_up[ascii_uppercase[k]] = dict_up[ascii_uppercase[k]] + 1

b=0
count = 0
for l in ascii_uppercase:
    if dict_up[l] > b:
        b = dict_up[l]
        c = l
for o in ascii_uppercase:
    if dict_up[o] == b:
        count += 1
if count == 1:
    print(c)
else:
    print("?")