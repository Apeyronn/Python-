print("""ATM sistemine hoşgeldiniz""")
print("""İşlem yapacağınız bankanızı seçiniz
1 - Denizbank
2 - Akbank
3 - Ziraat Bankası
""")

bankalar = [{"banka": "Denizbank", "bakiye": 1500.0, "sifre": "1234"},
            {"banka": "Akbank", "bakiye": 3000.0, "sifre": "12345"},
            {"banka": "Ziraat Bankası", "bakiye": 9000.0, "sifre": "12346"}]

while True:
    hak = 3
    secim = input("İşlemi giriniz (Çıkmak için 0'a basınız): ")
    if secim == "0":
        break
    elif secim in ["1", "2", "3"]:
        banka = bankalar[int(secim)-1]
        print(f"{banka['banka']} bankasını seçtiniz. Şifrenizi giriniz.")
        sifre = input("Şifre: ")
        if sifre == banka["sifre"]:
            print(f"Şifreniz doğru. Bakiyeniz: {banka['bakiye']}")
            print("""Yapmak istediğiniz işlemi seçin
            1 - Para Çekme
            2 - Para Yatırma
            """)
            islem = input("İstediğiniz işlem: ")
            if islem == "1":
                cekilecek_miktar = float(input("Çekmek istediğiniz miktarı girin: "))
                if cekilecek_miktar <= banka['bakiye']:
                    banka['bakiye'] -= cekilecek_miktar
                    print(f"{cekilecek_miktar} TL çektiniz. Yeni bakiyeniz: {banka['bakiye']}")
                else:
                    print("Yetersiz bakiye!")
            elif islem == "2":
                yatirilacak_miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
                banka['bakiye'] += yatirilacak_miktar
                print(f"{yatirilacak_miktar} TL yatırdınız. Yeni bakiyeniz: {banka['bakiye']}")
            else:
                print("Geçersiz işlem seçimi!")
        else:
                while hak > 1:
                    hak -= 1
                    print(f"Yanlış şifre girdiniz. {hak} hakkınız kaldı.")
                    sifre = input("Tekrar şifre giriniz: ")
                    if sifre == banka["sifre"]:
                        print(f"Şifreniz doğru. Bakiyeniz: {banka['bakiye']}")
                        print("""Yapmak istediğiniz işlemi seçin
                            1 - Para Çekme
                            2 - Para Yatırma
                            """)
                        islem = input("İstediğiniz işlem: ")
                        if islem == "1":
                            cekilecek_miktar = float(input("Çekmek istediğiniz miktarı girin: "))
                            if cekilecek_miktar <= banka['bakiye']:
                                banka['bakiye'] -= cekilecek_miktar
                                print(f"{cekilecek_miktar} TL çektiniz. Yeni bakiyeniz: {banka['bakiye']}")
                            else:
                                print("Yetersiz bakiye!")
                        elif islem == "2":
                            yatirilacak_miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
                            banka['bakiye'] += yatirilacak_miktar
                            print(f"{yatirilacak_miktar} TL yatırdınız. Yeni bakiyeniz: {banka['bakiye']}")
                        else:
                            print("Geçersiz işlem seçimi!")
                        break
                else:
                    print("Hatalı giriş sayısı aşıldı. Kartınız bloke oldu!")
                    break


