#########en buyuk sayi tespit etme######
list = [55 , 45, 30, 80, 75, 80, 10, 65, 35, 20, 90, 100]
enbuyuksayi = list[0]
for i in range(12):
    if list[i] > enbuyuksayi:
        enbuyuksayi = list[i]
print(enbuyuksayi)