
import csv

sem1_li = []
sem2_li = []

with open('saraksts_1.csv') as f:
    csv_reader1 = csv.reader(f, delimiter=',')
    for row in csv_reader1:
        sem1_li.append(tuple(row))
        
with open('saraksts_2.csv') as f:
    csv_reader2 = csv.reader(f, delimiter=',')
    for row in csv_reader2:
        sem2_li.append(tuple(row))
     
        
se1 = set(sem1_li)
se2 = set(sem2_li)
        
print("Only 1st seminar:", len((se1 - se2)))
print("Only 2nd seminar:", len((se2 - se1)))
print("Both seminars:", len((se2 & se1)))
        
header01 = ['Name', 'Surname', 'e-mail']
header02 = ['Name', 'Surname', 'e-mail', 'Workshop']

# attended both seminars and elegible for a certificate
with open('saraksts_sertifikatiem.csv' , 'w' , newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header01)
    for row in (se2 & se1):
        csv_writer.writerow(row)
    
# attended only 1 seminar and have to finsh the course   
with open('saraksts_turpinat.csv' , 'w' , newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header02)
    for row in (se1 - se2):
        csv_writer.writerow(row + ('1',))
    for row in (se2 - se1):
        csv_writer.writerow(row + ('2',))