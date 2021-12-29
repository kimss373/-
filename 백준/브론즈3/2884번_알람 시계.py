h, m = map(int, input().split())
alarm = h*60+m
wake = alarm-45
if wake<0:
    wake1 = wake+1440
else:
    wake1 = wake
print(wake1//60, wake1%60)