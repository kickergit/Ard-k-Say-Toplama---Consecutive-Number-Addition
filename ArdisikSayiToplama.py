#ardışık sayıları toplama gahos efendi
print("ARDIŞIK SAYILARI TOPLAMA")
toplam = 0
baslangic = int(input("Başlangıç (Tam sayı giriniz!):" ))
bitis = int(input("Bitiş (Tam sayı giriniz!):")) +1
artis = int(input("Artış Miktari (Tam sayı giriniz!)" ))
for a in range(baslangic, bitis, artis):
                toplam+=a
                print(a ,end=" +")
print("=",toplam)
