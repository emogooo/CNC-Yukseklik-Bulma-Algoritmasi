from random import randint
kkk = 5
yukseklikHaritasi =[]
sayi = 2
for i in range(sayi):
    yukseklikHaritasi.append([i] * sayi)
"""
yukseklikHaritasi[0][0] = 4  # Deneme amaçlı verilen değerdir.
yukseklikHaritasi[0][1] = 10  # Deneme amaçlı verilen değerdir.
yukseklikHaritasi[1][0] = 2  # Deneme amaçlı verilen değerdir.
yukseklikHaritasi[1][1] = 6  # Deneme amaçlı verilen değerdir.
"""

for i in range(sayi):
    for j in range(sayi):
        yukseklikHaritasi[j][i] = randint(0,500) / 100

def yukseklikBul(bulunacakX, bulunacakY):
    girdiBasamakDegeri = 1000000000
    hassasiyetDegeri = 0.01
    kareKenarUzunlugu = kkk * girdiBasamakDegeri

    if bulunacakX > ((len(yukseklikHaritasi[0]) - 1) * (kareKenarUzunlugu / girdiBasamakDegeri)) or bulunacakY > ((len(yukseklikHaritasi) - 1) * (kareKenarUzunlugu / girdiBasamakDegeri)):
        return "Hatalı değer.. gönderilen konum matrisin sahip olduğu bir konum olmalıdır."

    by = bulunacakY
    bx = bulunacakX

    bulunacakX *= girdiBasamakDegeri
    bulunacakY *= girdiBasamakDegeri

    """
    bulunacakX = float(bulunacakX)
    bulunacakY = float(bulunacakY)
    """
    kareX = int(bulunacakX / kareKenarUzunlugu)  # X düzlemindeki (kareX + 1)'inci kare
    kareY = int(bulunacakY / kareKenarUzunlugu)  # Y düzlemindeki (kareY + 1)' inci kare

    bulunacakX = bulunacakX % kareKenarUzunlugu  # Saptanan karenin içerisindeki X konumu
    bulunacakY = bulunacakY % kareKenarUzunlugu  # Saptanan karenin içerisindeki Y konumu

    if bx == ((len(yukseklikHaritasi[0]) - 1) * (kareKenarUzunlugu / girdiBasamakDegeri)):
        kareX -= 1
        bulunacakX = kareKenarUzunlugu

    if by == ((len(yukseklikHaritasi) - 1) * (kareKenarUzunlugu / girdiBasamakDegeri)):
        kareY -= 1
        bulunacakY = kareKenarUzunlugu

    ortaNoktaUstDegerX = kareKenarUzunlugu
    ortaNoktaAltDegerX = 0
    ortaNoktaUstDegerY = kareKenarUzunlugu
    ortaNoktaAltDegerY = 0

    nokta00 = yukseklikHaritasi[kareY][kareX]
    nokta10 = yukseklikHaritasi[kareY][kareX + 1]
    nokta01 = yukseklikHaritasi[kareY + 1][kareX]
    nokta11 = yukseklikHaritasi[kareY + 1][kareX + 1]

    ortaNokta = (nokta00 + nokta10 + nokta01 + nokta11) / 4
    ortaNoktaX = kareKenarUzunlugu / 2
    ortaNoktaY = kareKenarUzunlugu / 2

    if nokta00 == nokta10 and nokta10 == nokta01 and nokta01 == nokta11:   # 4 nokta eş ise tüm yüzey eştir.
        return ortaNokta

    """if bulunacakX == ortaNoktaX and bulunacakY == ortaNoktaY:  # Karenin ortası isteniliyorsa
        return ortaNokta
    """

    if bulunacakX == ortaNoktaX:  # X ekseninin ortasındaysa
        return yukseklikBul((bx + (bx / (girdiBasamakDegeri * 10))), by)
    if bulunacakY == ortaNoktaY:  # Y ekseninin ortasındaysa
        return yukseklikBul(bx, (by + (by / (girdiBasamakDegeri * 10))))

    while True:
        if abs(bulunacakX - ortaNoktaX) < hassasiyetDegeri and abs(bulunacakY - ortaNoktaY) < hassasiyetDegeri:
            return round(ortaNokta, 8)

        if bulunacakX < ortaNoktaX and bulunacakY < ortaNoktaY:  # Sol alt
            nokta10 = (nokta00 + nokta10) / 2
            nokta01 = (nokta00 + nokta01) / 2
            nokta11 = ortaNokta
            ortaNoktaUstDegerX = ortaNoktaX
            ortaNoktaUstDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaAltDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaAltDegerY) / 2

        elif bulunacakX > ortaNoktaX and bulunacakY < ortaNoktaY:  # Sağ alt
            nokta00 = (nokta00 + nokta10) / 2
            nokta01 = ortaNokta
            nokta11 = (nokta10 + nokta11) / 2
            ortaNoktaAltDegerX = ortaNoktaX
            ortaNoktaUstDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaUstDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaAltDegerY) / 2

        elif bulunacakX < ortaNoktaX and bulunacakY > ortaNoktaY:  # Sol üst
            nokta00 = (nokta00 + nokta01) / 2
            nokta10 = ortaNokta
            nokta11 = (nokta01 + nokta11) / 2
            ortaNoktaUstDegerX = ortaNoktaX
            ortaNoktaAltDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaAltDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaUstDegerY) / 2

        elif bulunacakX > ortaNoktaX and bulunacakY > ortaNoktaY:  # Sağ üst
            nokta00 = ortaNokta
            nokta10 = (nokta10 + nokta11) / 2
            nokta01 = (nokta01 + nokta11) / 2
            ortaNoktaAltDegerX = ortaNoktaX
            ortaNoktaAltDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaUstDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaUstDegerY) / 2

        elif bulunacakX == ortaNoktaX:  # X ekseninin ortasındaysa
            return yukseklikBul((bx + (bx / (girdiBasamakDegeri * 100))), by)

        elif bulunacakY == ortaNoktaY:  # Y ekseninin ortasındaysa
            return yukseklikBul(bx, (by + (by / (girdiBasamakDegeri * 100))))

        ortaNokta = (nokta00 + nokta10 + nokta01 + nokta11) / 4
        # print(ortaNokta)



def test():
    basamak = 10
    kbp = kkk * basamak #Karenin bölünceği parça
    hataSayaci = 0
    for i in range((kbp + 1)):
        ilkKonum = yukseklikBul((i / basamak), (1 / basamak))
        ikinciKonum = yukseklikBul((i / basamak), (2 / basamak))
        baslangicFarki = abs(ikinciKonum - ilkKonum)
        print("---------------------" + str(round(baslangicFarki,5)) + "---------------------")

        for j in range((kbp + 1)):
            if kbp == j:
                simdiki = yukseklikBul((i / basamak), (j / basamak))
                onceki = yukseklikBul((i / basamak), ((j - 1) / basamak))
                simdikiFark = abs(simdiki - onceki)
            else:
                simdiki = yukseklikBul((i / basamak), (j / basamak))
                sonraki = yukseklikBul((i / basamak), ((j + 1) / basamak))
                simdikiFark = abs(simdiki - sonraki)

            hassasiyet = abs(baslangicFarki - simdikiFark)
            print(str(i / basamak) + " - " + str(j / basamak) + " noktalarının yüksekliği: "+ str(simdiki))
            if hassasiyet > 0.00001:
                if j % basamak == 0:
                    continue
                else:
                    hataSayaci += 1

    print("Hatalı değer: " + str(hataSayaci))

test()
#print(yukseklikBul(5,5))