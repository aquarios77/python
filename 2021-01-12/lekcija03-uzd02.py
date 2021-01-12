mark = int(input("Enter a mark 0..100: "))
a_start = 100
a_end = 90
b_start = 89
b_end = 80
c_start = 79
c_end = 70
d_start = 69
d_end = 60
e_start = 59
e_end = 50
f_start = 49
f_end = 0

if(mark>100 or mark<0): print("wrong mark!")
elif(a_start>=mark>=a_end): print("A grade!")
elif(b_start>=mark>=b_end): print("B grade!")
elif(c_start>=mark>=c_end): print("C grade!")
elif(d_start>=mark>=d_end): print("D grade!")
elif(e_start>=mark>=e_end): print("E grade!")
else: print("F grade :( ")