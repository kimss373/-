mushroom = []

for i in range(10):
    mushroom.append(int(input()))

now = 0
for i in range(10):
    if now + mushroom[i] > 100:
        if abs(100-now) >= abs(100-now-mushroom[i]):
            now += mushroom[i]
            break
        else:
            break
    now += mushroom[i]

print(now)