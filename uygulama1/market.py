def toplam_goster(urun):
    urun = urun[:-1]
    liste = urun.split(' ')
    
    urun_name = liste[0]
    satislar = liste[1].split(',')
    
    ocak = int(satislar[0])
    subat = int(satislar[1])
    mart = int(satislar[2])
    performans = ""
    ortalama_satis = (ocak+subat+mart)/3
    if ortalama_satis>=374:
        performans= "çok iyi"
    elif ortalama_satis>199 and ortalama_satis<374:
        performans = "iyi"
    elif ortalama_satis<100:
        performans = "kötü"

    return urun_name + ": " + performans + "\n"   

def urun_bazinda_goster():
    with open("satis_miktari2.txt", "r", encoding="utf=8") as file:
        for urun in file: 
            print((toplam_goster(urun)))
def satislari_gir():
    urun_adi = input("lütfen ürün adını girin: ")
    ocak_ayi = input("lütfen ocak ayi satislari girin: ")
    subat_ayi = input("lütfen subat ayi satislari girin: ")
    mart_ayi = input("lütfen mart ayi satislari girin: ")
    
    with open("satis_miktari2.txt", "a", encoding="utf-8") as file:
        file.write(urun_adi+" "+ocak_ayi+ "," + subat_ayi+ "," + mart_ayi+"\n")
def satislari_kaydet():
    with open(r'satis_miktari2.txt', encoding="utf-8") as file:
        liste =[]

        for i in file: 
            liste.append(toplam_goster(i))
        
        with open("rapor.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)
while True:
    islem = int(input("1- satışları göster\n2-satışları gir\n3- satışarı kaydet\n4-çıkış\n"))

    if islem == 1: 
        urun_bazinda_goster()
    elif islem == 2:
        satislari_gir() 
    elif islem == 3:
        satislari_kaydet()
    else: 
        break