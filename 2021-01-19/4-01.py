n = 5
i = 1
summa = 0
print("Enter a mark: ")
while i<=n:
    mark = int(input("==> "))
    if mark >10 or mark<=0:
        print("Mark is incorrect! Enter one more time: ")
        continue
    summa += mark
    i+=1
print(summa/n)