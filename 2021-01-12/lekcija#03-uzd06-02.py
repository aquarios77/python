seconds = int(input('Ievadiet sekundes: '))

hours = seconds//3600
seconds_left = seconds%3600
minutes = seconds_left//60
seconds_left = seconds_left%60

print(hours,minutes,seconds_left)