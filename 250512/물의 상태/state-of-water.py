temp = int(input())

if temp < 0:
    print('ice')
elif temp >= 0 and temp < 100:
    print('water')
else:
    print('vapor')