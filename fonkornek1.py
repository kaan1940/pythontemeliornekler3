##########kombinasyon hesaplama ornegi######
def faktoriyel(sayi):
    faktoriyelsonuc = 1 
    for i in range(1, sayi + 1):
        faktoriyelsonuc = faktoriyelsonuc * i
    return faktoriyelsonuc
print("n gir")
n = int(input())
print("r gir")
r = int(input())
nfakt = faktoriyel(n)
rfakt = faktoriyel(r)
neksirfakt = faktoriyel(n - r)
sonuc = nfakt / (rfakt * neksirfakt)
print("C(6, 3) sonucu: " + str(sonuc))