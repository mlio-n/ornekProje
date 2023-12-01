KATSAYI = 1

def Kat_Katsayi_Degistir(katsayi):
    global KATSAYI
    if katsayi == 1: #ara kat
        KATSAYI *= 2
    elif katsayi == 2:
        KATSAYI *= 1.6 #ust kat
    else:
        KATSAYI *= 0.9 #zemin kat
    return KATSAYI

def Metrekare(en, boy):
    metrekare = en*boy
    return metrekare

def Fiyat_Hesaplayici(katsayi, metrekare):
    fiyat = katsayi * metrekare * 5000
    return fiyat
