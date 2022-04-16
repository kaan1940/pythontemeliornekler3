########toplam sembolu hesaplama ornegi######
def seritoplami(bas, son):
    seritoplam = 0
    for i in range(bas, son + 1, 1):
        seritoplam = seritoplam + i
    
    return seritoplam

toplam = 0
print("sayi1bas degeri gir")
sayi1bas = int(input())
print("sayi1son degeri gir")
sayi1son = int(input())
print("sayi2bas degeri gir")
sayi2bas = int(input())
print("sayi2son degeri gir")
sayi2son = int(input())
print("sayi3bas degeri gir")
sayi3bas = int(input())
print("sayi3son degeri gir")
sayi3son = int(input())
toplam = seritoplami(sayi1bas, sayi1son) + seritoplami(sayi2bas, sayi2son) + seritoplami(sayi3bas, sayi3son)
print("toplam sonucu: " + str(toplam))

