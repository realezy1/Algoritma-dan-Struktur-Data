#no1 B
import re
pola = r'[\w.-]+@[\w.-]+'
string = "Marsha memiliki no.handphone 08211111111 dan email marsha_11@gmail.com"
cari = re.findall(pola, string)
print(cari)
print(cari[0])

#no1 D
pola = re.findall(r'\d+', string)
print(pola[0])