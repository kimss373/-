burger=[]
beverage=[]
for i in range(3):
    burger.append(int(input()))
for i in range(2):
    beverage.append(int(input()))
burger.sort()
beverage.sort()
print(burger[0]+beverage[0]-50)