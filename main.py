girdiBasamakDegeri = 1000000000
kareKenarUzunlugu = 5 * girdiBasamakDegeri  # 5 milimetreyi temsil etmektedir.
kartEn = 200 * girdiBasamakDegeri  # 200 milimetreyi temsil etmektedir.
kartBoy = 100 * girdiBasamakDegeri  # 100 milimetreyi temsil etmektedir.
yukseklikHaritasi = [[0 for i in range(int(kartBoy / kareKenarUzunlugu))] for i in
                     range(int(kartEn / kareKenarUzunlugu))]

yukseklikHaritasi[0][0] = 5  # Deneme amaçlı verilen değerdir.
yukseklikHaritasi[1][0] = 4  # Deneme amaçlı verilen değerdir.
yukseklikHaritasi[0][1] = 6  # Deneme amaçlı verilen değerdir.
yukseklikHaritasi[1][1] = 1  # Deneme amaçlı verilen değerdir.

def yukseklikBul(bulunacakX, bulunacakY, hassasiyetDegeri=0.01):
    nokta1, nokta2, nokta3, nokta4 = 0, 0, 0, 0  # Sırasıyla 00,10,01,11 noktlarını temsil etmektedir.
    by = bulunacakY
    bx = bulunacakX
    bulunacakX *= girdiBasamakDegeri
    bulunacakY *= girdiBasamakDegeri
    bulunacakX = float(bulunacakX)
    bulunacakY = float(bulunacakY)
    kareX = int(bulunacakX / kareKenarUzunlugu)  # X düzlemindeki (kareX + 1)'inci kare
    kareY = int(bulunacakY / kareKenarUzunlugu)  # Y düzlemindeki (kareY + 1)' inci kare
    bulunacakX = float(bulunacakX % kareKenarUzunlugu)  # Saptanan karenin içerisindeki X konumu
    bulunacakY = float(bulunacakY % kareKenarUzunlugu)  # Saptanan karenin içerisindeki Y konumu
    ortaNoktaUstDegerX = kareKenarUzunlugu
    ortaNoktaAltDegerX = 0
    ortaNoktaUstDegerY = kareKenarUzunlugu
    ortaNoktaAltDegerY = 0
    ortaNokta = (yukseklikHaritasi[kareX][kareY] + yukseklikHaritasi[kareX + 1][kareY] + yukseklikHaritasi[kareX][
        kareY + 1] + yukseklikHaritasi[kareX + 1][kareY + 1]) / 4
    ortaNoktaX = kareKenarUzunlugu / 2
    ortaNoktaY = kareKenarUzunlugu / 2

    if yukseklikHaritasi[kareX][kareY] == yukseklikHaritasi[kareX + 1][kareY] and yukseklikHaritasi[kareX + 1][kareY] == \
            yukseklikHaritasi[kareX][kareY + 1] and yukseklikHaritasi[kareX][kareY + 1] == yukseklikHaritasi[kareX + 1][
        kareY + 1]:
        return ortaNokta  # 4 nokta eş ise tüm yüzey eştir.

    if bulunacakX == ortaNoktaX and bulunacakY == ortaNoktaY:  # Karenin ortası isteniliyorsa
        return ortaNokta

    if bulunacakX < ortaNoktaX and bulunacakY < ortaNoktaY:  # Sol alt
        nokta1 = yukseklikHaritasi[kareX][kareY]
        nokta2 = (yukseklikHaritasi[kareX][kareY] + yukseklikHaritasi[kareX + 1][kareY]) / 2
        nokta3 = (yukseklikHaritasi[kareX][kareY] + yukseklikHaritasi[kareX][kareY + 1]) / 2
        nokta4 = ortaNokta
        ortaNoktaUstDegerX = ortaNoktaX
        ortaNoktaUstDegerY = ortaNoktaY
        ortaNoktaX = (ortaNoktaX + ortaNoktaAltDegerX) / 2
        ortaNoktaY = (ortaNoktaY + ortaNoktaAltDegerY) / 2

    elif bulunacakX > ortaNoktaX and bulunacakY < ortaNoktaY:  # Sağ alt
        nokta1 = (yukseklikHaritasi[kareX][kareY] + yukseklikHaritasi[kareX + 1][kareY]) / 2
        nokta2 = yukseklikHaritasi[kareX + 1][kareY]
        nokta3 = ortaNokta
        nokta4 = (yukseklikHaritasi[kareX + 1][kareY] + yukseklikHaritasi[kareX + 1][kareY + 1]) / 2
        ortaNoktaAltDegerX = ortaNoktaX
        ortaNoktaUstDegerY = ortaNoktaY
        ortaNoktaX = (ortaNoktaX + ortaNoktaUstDegerX) / 2
        ortaNoktaY = (ortaNoktaY + ortaNoktaAltDegerY) / 2

    elif bulunacakX < ortaNoktaX and bulunacakY > ortaNoktaY:  # Sol üst
        nokta1 = (yukseklikHaritasi[kareX][kareY] + yukseklikHaritasi[kareX][kareY + 1]) / 2
        nokta2 = ortaNokta
        nokta3 = yukseklikHaritasi[kareX][kareY + 1]
        nokta4 = (yukseklikHaritasi[kareX][kareY + 1] + yukseklikHaritasi[kareX + 1][kareY + 1]) / 2
        ortaNoktaUstDegerX = ortaNoktaX
        ortaNoktaAltDegerY = ortaNoktaY
        ortaNoktaX = (ortaNoktaX + ortaNoktaAltDegerX) / 2
        ortaNoktaY = (ortaNoktaY + ortaNoktaUstDegerY) / 2

    elif bulunacakX > ortaNoktaX and bulunacakY > ortaNoktaY:  # Sağ üst
        nokta1 = ortaNokta
        nokta2 = (yukseklikHaritasi[kareX + 1][kareY] + yukseklikHaritasi[kareX + 1][kareY + 1]) / 2
        nokta3 = (yukseklikHaritasi[kareX][kareY + 1] + yukseklikHaritasi[kareX + 1][kareY + 1]) / 2
        nokta4 = yukseklikHaritasi[kareX + 1][kareY + 1]
        ortaNoktaAltDegerX = ortaNoktaX
        ortaNoktaAltDegerY = ortaNoktaY
        ortaNoktaX = (ortaNoktaX + ortaNoktaUstDegerX) / 2
        ortaNoktaY = (ortaNoktaY + ortaNoktaUstDegerY) / 2

    elif bulunacakX == ortaNoktaX:  # X ekseninin ortasındaysa
        return yukseklikBul((bx + (bx / (girdiBasamakDegeri * 10))), by, hassasiyetDegeri)

    elif bulunacakY == ortaNoktaY:  # Y ekseninin ortasındaysa
        return yukseklikBul(bx, (by + (by / (girdiBasamakDegeri * 10))), hassasiyetDegeri)

    while True:
        ortaNokta = (nokta1 + nokta2 + nokta3 + nokta4) / 4
        # print(ortaNokta)
        if abs(bulunacakX - ortaNoktaX) < hassasiyetDegeri and abs(bulunacakY - ortaNoktaY) < hassasiyetDegeri:
            return round(ortaNokta, 5)

        if bulunacakX < ortaNoktaX and bulunacakY < ortaNoktaY:  # Sol alt
            nokta2 = (nokta1 + nokta2) / 2
            nokta3 = (nokta1 + nokta3) / 2
            nokta4 = ortaNokta
            ortaNoktaUstDegerX = ortaNoktaX
            ortaNoktaUstDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaAltDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaAltDegerY) / 2

        elif bulunacakX > ortaNoktaX and bulunacakY < ortaNoktaY:  # Sağ alt
            nokta1 = (nokta1 + nokta2) / 2
            nokta3 = ortaNokta
            nokta4 = (nokta2 + nokta4) / 2
            ortaNoktaAltDegerX = ortaNoktaX
            ortaNoktaUstDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaUstDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaAltDegerY) / 2

        elif bulunacakX < ortaNoktaX and bulunacakY > ortaNoktaY:  # Sol üst
            nokta1 = (nokta1 + nokta3) / 2
            nokta2 = ortaNokta
            nokta4 = (nokta3 + nokta4) / 2
            ortaNoktaUstDegerX = ortaNoktaX
            ortaNoktaAltDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaAltDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaUstDegerY) / 2

        elif bulunacakX > ortaNoktaX and bulunacakY > ortaNoktaY:  # Sağ üst
            nokta1 = ortaNokta
            nokta2 = (nokta2 + nokta4) / 2
            nokta3 = (nokta3 + nokta4) / 2
            ortaNoktaAltDegerX = ortaNoktaX
            ortaNoktaAltDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaUstDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaUstDegerY) / 2

        elif bulunacakX == ortaNoktaX:  # X ekseninin ortasındaysa
            return yukseklikBul((bx + (bx / (girdiBasamakDegeri * 100))), by, hassasiyetDegeri)

        elif bulunacakY == ortaNoktaY:  # Y ekseninin ortasındaysa
            return yukseklikBul(bx, (by + (by / (girdiBasamakDegeri * 100))), hassasiyetDegeri)


def testEt():
    kbp = 50 #Karenin bölünceği parça
    hataSayaci = 0

    for i in range((kbp + 1)):
        ilkKonum = yukseklikBul((i / (kbp / 5)), (1 / (kbp / 5)))
        ikinciKonum = yukseklikBul((i / (kbp / 5)), (2 / (kbp / 5)))
        baslangicFarki = abs(ikinciKonum - ilkKonum)
        print("---------------------" + str(round(baslangicFarki,5)) + "---------------------")

        for j in range((kbp + 1)):
            simdiki = yukseklikBul((i / (kbp / 5)), (j / (kbp / 5)))
            sonraki = yukseklikBul((i / (kbp / 5)), ((j + 1) / (kbp / 5)))
            simdikiFark = abs(simdiki - sonraki)
            hassasiyet = abs(baslangicFarki - simdikiFark)
            print(str(i / (kbp / 5)) + " - " + str(j / (kbp / 5)) + " noktalarının yüksekliği: "+ str(simdiki))
            if hassasiyet > 0.00000001:
                if j % (kbp / 5) == 0:
                    hataSayaci
                else:
                    hataSayaci += 1

    print("Hatalı değer: " + str(hataSayaci))

testEt()