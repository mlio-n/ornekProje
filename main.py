import arsa
import daire

def Main():
    cikis = 'h' #Dongu baslangici icin
    while cikis != 'E' and cikis != 'e': # 'E' ve 'e' girilmediği sürece devam et
        Menu_Goruntule()
    #('1 - Arsa islemleri icin')
    #('2 - Daire islemleri icin')

        secim = Sayi_Al(1,2)
        if secim == 1:
            print('Arsanizin konumu [1-Deniz Kenari, 2-Sehir Merkezi, 3-Kirsal Arazi]')
            konum = Sayi_Al(1,3)
            arsa_katsayisi = arsa.Katsayi_Degistir(konum)

            print('Arsanizin sekli [1-Dikdortgen, 2-Daire]')
            sekil = Sayi_Al(1,2)
            if sekil == 1:
                print('Dikdortgenin eni: ')
                en = Sayi_Al(1,1000) # metre
                print('Dikdortgenin boyu: ')
                boy = Sayi_Al(1, 1000) # metre
                dikdortgen_cevresi = arsa.Dikdortgen_Cevre(en, boy)
                fiyat = arsa.Fiyat_Hesaplayici(arsa_katsayisi, dikdortgen_cevresi)
                print(f'Arsanin fiyati: {fiyat:,.0f}TL.')
            else:
                print('Daire seklindeki arsanin yaricapi: ')
                yaricap = Sayi_Al(1, 1000)
                cember_cevre = arsa.Cember_Cevre(yaricap)
                fiyat = arsa.Fiyat_Hesaplayici(arsa_katsayisi, cember_cevre)
                print(f'Arsanin fiyati: {fiyat:,.0f}TL.')

        else:
            print('Dairenin kat ozelligi: [1-Ara kat, 2-Ust kat, 3-Zemin kat')
            kat_konum = Sayi_Al(1, 3)
            kat_katsayisi = daire.Kat_Katsayi_Degistir(kat_konum)
            print('Dairenin eni: ')
            en = Sayi_Al(1, 1000)
            print('Dairenin boyu: ')
            boy = Sayi_Al(1, 1000)
            daire_alani = daire.Metrekare(en, boy)
            fiyat = daire.Fiyat_Hesaplayici(kat_katsayisi,daire_alani)
            print(f'Dairenin fiyati: {fiyat:,.0f}TL.')

        cikis = input('İsleminiz bitmistir. Cikmak icin (E/e) basin. Tekrar fiyat hesaplamasi icin (H/h) basin: ')
        if cikis != 'e' and cikis != 'E' and cikis != 'h' and cikis != 'H':
            break
        elif cikis == 'e' or cikis == 'E':
            print('Hoscakalin!')

#-----------------------------Yardimci fonksiyonlar ---------------------------------------------------------------
def Sayi_Al(altSinir, ustSinir):
    sayi = int(input())
    while sayi < altSinir or sayi > ustSinir:
        sayi = int(input('Hatali sayi. Tekrar giriniz.'))
    return sayi

def Menu_Goruntule():
    print('1 - Arsa islemleri icin')
    print('2 - Daire islemleri icin')
#----------------------------------------------------------------------------------------------------------------------

Main()




