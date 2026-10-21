seriler = []
sayac = 0
i = 0
fazlalik = 0
fiyat = 20

for i in range(5):
    a = int(input("Serinin " + str(i+1) + ". kitabından kaç tane almak istersiniz? : "))
    seriler.append(a)

c = 0
while c < len(seriler):
    if (seriler[c] > 0):
        sayac += 1
    if (seriler[c] > 1):
        fazlalik = fazlalik + (seriler[c] - 1)
    c += 1

if(sayac == 2):
    toplam = fazlalik*fiyat + sayac*fiyat*0.90

elif(sayac == 3):
    toplam = fazlalik*fiyat + sayac*fiyat*0.85

elif(sayac == 4):
    toplam = fazlalik*fiyat + sayac*fiyat*0.80

elif(sayac == 5):
    toplam = fazlalik*fiyat + sayac*fiyat*0.75

print("Toplam ödemeniz gereken tutar: " + str(toplam) + " TL")
