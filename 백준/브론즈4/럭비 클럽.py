while True:
    name, age, weight = map(str, input().split())
    if name == '#' and age == '0' and weight == '0':
        break
    if int(age) <= 17 and int(weight) < 80:
        print(name, 'Junior')
    else:
        print(name, 'Senior')
