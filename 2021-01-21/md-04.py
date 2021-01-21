number = abs(int(input("Enter a positive integer: ")))
counter=1
faktor=1
print(number,"!=",end='',sep='')
while counter<=number:
  print(counter,end='',sep='')
  if counter!=number:
      print('*',end='',sep='')
  faktor*=counter
  counter+=1
print('=',faktor,sep='')
