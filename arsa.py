KATSAYI = 1

def Katsayi_Degistir(katsayi):
    global KATSAYI
    if katsayi == 1:
        KATSAYI *= 1.6 #deniz kenari
    elif katsayi == 2:
        KATSAYI *= 1.2 #sehir merkezi
    else:
        KATSAYI *= 0.8 #arazi
    return KATSAYI

def Dikdortgen_Cevre(en,boy):
    cevre = 2*(en + boy)
    return cevre

def Cember_Cevre(yaricap):
    return 2*3.14*yaricap

def Fiyat_Hesaplayici(katsayi, cevre):
    fiyat = katsayi * cevre * 1000
    return fiyat