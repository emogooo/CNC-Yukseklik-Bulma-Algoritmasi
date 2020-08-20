
girdiBasamakDegeri = 100
"""
10 üzeri n değerler giriniz.
n, virgülden sonra kaç basamakta sayı verebileceğinizi belirtir.
n ne kadar büyürse o kadar hassas işlem yapabilirsiniz.

Örneğin: girdiBasamakDegeri = 100 için (1.56, 3.69) noktaları hesaplanabilir fakat (1.561, 3.696) noktaları hesaplanamaz
"""

kareKenarUzunlugu = 5 * girdiBasamakDegeri       #5 milimetreyi temsil etmektedir.
kartEn = 200 * girdiBasamakDegeri      #200 milimetreyi temsil etmektedir.
kartBoy = 100 * girdiBasamakDegeri      #100 milimetreyi temsil etmektedir.
yukseklikHaritasi = [[0 for i in range(int(kartBoy/kareKenarUzunlugu))] for i in range(int(kartEn/kareKenarUzunlugu))]


yukseklikHaritasi[0][0] = 2     #Deneme amaçlı verilen değerdir.
yukseklikHaritasi[1][0] = 1     #Deneme amaçlı verilen değerdir.
yukseklikHaritasi[0][1] = 3     #Deneme amaçlı verilen değerdir.
yukseklikHaritasi[1][1] = 2     #Deneme amaçlı verilen değerdir.


def yukseklikBul(bulunacakX, bulunacakY, hassasiyetDegeri = 0.1):
    nokta1, nokta2, nokta3, nokta4 = 0, 0, 0, 0     #Sırasıyla 00,10,01,11 noktlarını temsil etmektedir.
    bulunacakX *= girdiBasamakDegeri
    bulunacakY *= girdiBasamakDegeri
    kareX = int(bulunacakX / kareKenarUzunlugu)     #X düzlemindeki (kareX + 1)'inci kare
    kareY = int(bulunacakY / kareKenarUzunlugu)      #Y düzlemindeki (kareY + 1)' inci kare
    kareKonumX = int(bulunacakX % kareKenarUzunlugu)    #Saptanan karenin içerisindeki X konumu
    kareKonumY = int(bulunacakY % kareKenarUzunlugu)    #Saptanan karenin içerisindeki Y konumu
    ortaNoktaUstDegerX = kareKenarUzunlugu
    ortaNoktaAltDegerX = 0
    ortaNoktaUstDegerY = kareKenarUzunlugu
    ortaNoktaAltDegerY = 0
    ortaNokta = (yukseklikHaritasi[kareX][kareY] + yukseklikHaritasi[kareX + 1][kareY] + yukseklikHaritasi[kareX][kareY + 1] + yukseklikHaritasi[kareX + 1][kareY + 1]) / 4
    ortaNoktaX = kareKenarUzunlugu / 2
    ortaNoktaY = kareKenarUzunlugu / 2

    if yukseklikHaritasi[kareX][kareY] == yukseklikHaritasi[kareX + 1][kareY] and yukseklikHaritasi[kareX + 1][kareY] == yukseklikHaritasi[kareX][kareY + 1] and yukseklikHaritasi[kareX][kareY + 1] == yukseklikHaritasi[kareX + 1][kareY + 1]:
        return ortaNokta    #4 nokta eş ise tüm yüzey eştir.

    if kareKonumX < ortaNoktaX and kareKonumY < ortaNoktaY:     #Sol alt
        nokta1 = yukseklikHaritasi[kareX][kareY]
        nokta2 = (yukseklikHaritasi[kareX][kareY] + yukseklikHaritasi[kareX + 1][kareY]) / 2
        nokta3 = (yukseklikHaritasi[kareX][kareY] + yukseklikHaritasi[kareX][kareY + 1]) / 2
        nokta4 = ortaNokta
        ortaNoktaUstDegerX = ortaNoktaX
        ortaNoktaUstDegerY = ortaNoktaY
        ortaNoktaX = (ortaNoktaX + ortaNoktaAltDegerX) / 2
        ortaNoktaY = (ortaNoktaY + ortaNoktaAltDegerY) / 2

    elif kareKonumX > ortaNoktaX and kareKonumY < ortaNoktaY:   #Sağ alt
        nokta1 = (yukseklikHaritasi[kareX][kareY] + yukseklikHaritasi[kareX + 1][kareY]) / 2
        nokta2 = yukseklikHaritasi[kareX + 1][kareY]
        nokta3 = ortaNokta
        nokta4 = (yukseklikHaritasi[kareX + 1][kareY] + yukseklikHaritasi[kareX + 1][kareY + 1]) / 2
        ortaNoktaAltDegerX = ortaNoktaX
        ortaNoktaUstDegerY = ortaNoktaY
        ortaNoktaX = (ortaNoktaX + ortaNoktaUstDegerX) / 2
        ortaNoktaY = (ortaNoktaY + ortaNoktaAltDegerY) / 2

    elif kareKonumX < ortaNoktaX and kareKonumY > ortaNoktaY:   #Sol üst
        nokta1 = (yukseklikHaritasi[kareX][kareY] + yukseklikHaritasi[kareX][kareY + 1]) / 2
        nokta2 = ortaNokta
        nokta3 = yukseklikHaritasi[kareX][kareY + 1]
        nokta4 = (yukseklikHaritasi[kareX][kareY + 1] + yukseklikHaritasi[kareX + 1][kareY + 1]) / 2
        ortaNoktaUstDegerX = ortaNoktaX
        ortaNoktaAltDegerY = ortaNoktaY
        ortaNoktaX = (ortaNoktaX + ortaNoktaAltDegerX) / 2
        ortaNoktaY = (ortaNoktaY + ortaNoktaUstDegerY) / 2

    elif kareKonumX > ortaNoktaX and kareKonumY > ortaNoktaY:   #Sağ üst
        nokta1 = ortaNokta
        nokta2 = (yukseklikHaritasi[kareX + 1][kareY] + yukseklikHaritasi[kareX + 1][kareY + 1]) / 2
        nokta3 = (yukseklikHaritasi[kareX][kareY + 1] + yukseklikHaritasi[kareX + 1][kareY + 1]) / 2
        nokta4 = yukseklikHaritasi[kareX + 1][kareY + 1]
        ortaNoktaAltDegerX = ortaNoktaX
        ortaNoktaAltDegerY = ortaNoktaY
        ortaNoktaX = (ortaNoktaX + ortaNoktaUstDegerX) / 2
        ortaNoktaY = (ortaNoktaY + ortaNoktaUstDegerY) / 2

    while True:
        ortaNokta = (nokta1 + nokta2 + nokta3 + nokta4) / 4
        print(ortaNokta)
        if abs(bulunacakX - ortaNoktaX) < hassasiyetDegeri and abs(bulunacakY - ortaNoktaY) < hassasiyetDegeri:
            return ortaNokta

        if kareKonumX < ortaNoktaX and kareKonumY < ortaNoktaY:  #Sol alt
            nokta2 = (nokta1 + nokta2) / 2
            nokta3 = (nokta1 + nokta3) / 2
            nokta4 = ortaNokta
            ortaNoktaUstDegerX = ortaNoktaX
            ortaNoktaUstDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaAltDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaAltDegerY) / 2

        elif kareKonumX > ortaNoktaX and kareKonumY < ortaNoktaY:  #Sağ alt
            nokta1 = (nokta1 + nokta2) / 2
            nokta3 = ortaNokta
            nokta4 = (nokta2 + nokta4) / 2
            ortaNoktaAltDegerX = ortaNoktaX
            ortaNoktaUstDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaUstDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaAltDegerY) / 2

        elif kareKonumX < ortaNoktaX and kareKonumY > ortaNoktaY:  #Sol üst
            nokta1 = (nokta1 + nokta3) / 2
            nokta2 = ortaNokta
            nokta4 = (nokta3 + nokta4) / 2
            ortaNoktaUstDegerX = ortaNoktaX
            ortaNoktaAltDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaAltDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaUstDegerY) / 2

        elif kareKonumX > ortaNoktaX and kareKonumY > ortaNoktaY:  #Sağ üst
            nokta1 = ortaNokta
            nokta2 = (nokta2 + nokta4) / 2
            nokta3 = (nokta3 + nokta4) / 2
            ortaNoktaAltDegerX = ortaNoktaX
            ortaNoktaAltDegerY = ortaNoktaY
            ortaNoktaX = (ortaNoktaX + ortaNoktaUstDegerX) / 2
            ortaNoktaY = (ortaNoktaY + ortaNoktaUstDegerY) / 2


"""
3. parametre işlem hassaslığıdır.
Default değeri : 0.1
Bu sayıyı küçülterek daha net sonuçlar alabilirsiniz.
"""
print("Verilen noktanın yüksekliği : " + str(yukseklikBul(1,4)))