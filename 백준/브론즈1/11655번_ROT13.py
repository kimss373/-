from string import ascii_uppercase
from string import ascii_lowercase
upper = ascii_uppercase
lower = ascii_lowercase
a=input()
for i in range(len(a)):
    if a[i] in upper:
        b = upper.index(a[i])
        if b+13>=26:
            print(upper[b-13], end="")
        else:
            print(upper[b+13], end="")

    elif a[i] in lower:
        b = lower.index(a[i])
        if b+13>=26:
            print(lower[b - 13], end="")
        else:
            print(lower[b+13], end="")
    else:
        print(a[i],  end="")