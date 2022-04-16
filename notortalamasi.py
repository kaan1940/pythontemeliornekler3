#########girilen notlarin ortalamasi hesaplandi###########
notlar = [0] * 5
nottoplami = 0
for i in range(5):
    notlar[i] = int(input())
for i in range(5):
    nottoplami += notlar[i]
ortalama = nottoplami / 5
print(ortalama)