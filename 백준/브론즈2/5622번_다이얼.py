from string import ascii_uppercase
dict_ascii_uppercase = {}
for i in ascii_uppercase:
    if i == "A" or i== "B" or i== "C":
        dict_ascii_uppercase[i] = 3
    elif i == "D" or i == "E" or i == "F":
        dict_ascii_uppercase[i] = 4
    elif i == "G" or i == "H" or i == "I":
        dict_ascii_uppercase[i] = 5
    elif i == "J" or i == "K" or i == "L":
        dict_ascii_uppercase[i] = 6
    elif i == "M" or i == "N" or i == "O":
        dict_ascii_uppercase[i] = 7
    elif i == "P" or i == "Q" or i == "R" or i == "S":
        dict_ascii_uppercase[i] = 8
    elif i == "T" or i == "U" or i == "V":
        dict_ascii_uppercase[i] = 9
    elif i == "W" or i == "X" or i == "Y" or i == "Z":
        dict_ascii_uppercase[i] = 10

dial = list(map(str, input()))
ee=0
for i in dial:
    ee += dict_ascii_uppercase[i]
print(ee)