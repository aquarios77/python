stundas1 = int(input("Ievadiet stundas: "))
minutes1 = int(input('Ievadiet minutes: '))
sekundes1 = int(input('Ievadiet sekundes: '))

stundas2 = int(input("Ievadiet stundas: "))
minutes2 = int(input('Ievadiet minutes: '))
sekundes2 = int(input('Ievadiet sekundes: '))

sekundes_total1 = stundas1*3600 + minutes1*60 + sekundes1
sekundes_total2 = stundas2*3600 + minutes2*60 + sekundes2

if(sekundes_total1 > sekundes_total2): print(sekundes_total1 - sekundes_total2)
else: print(sekundes_total2 - sekundes_total1 )