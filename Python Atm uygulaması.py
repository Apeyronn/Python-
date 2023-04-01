print("""ATM sistemine hoşgeldiniz
Bankanızı seçiniz:
1- Denizbank
2- Akbank
3- Ziraat Bankası
Ekle- Yeni banka kartı ekle
""")
bankalar= [{"Banka":"Denizbank","Bakiye":3000,"Sifre":"erdem1"},{"Banka":"Akbank","Bakiye":6000,"Sifre":"erdem12"},{"Banka":"Ziraat","Bakiye":9000,"Sifre":"erdem123"}]

while True:
    hak=3
    secim=input("bir seçim yapınız:")

    if secim == "Ekle":
        yeni_banka = {}
        yeni_banka["Banka"] = input("Yeni banka adını giriniz: ")
        yeni_banka["Bakiye"] = float(input("Hesap bakiyesini giriniz: "))
        yeni_banka["Sifre"] = input("Şifreyi giriniz: ")
        bankalar.append(yeni_banka)
        print(f"Yeni banka başarıyla eklendi! bakiyeniz {yeni_banka['Bakiye']} tl dir")
        continue

    banka= bankalar[int(secim)-1]
    print(f"{banka['Banka']} bankasını seçtiniz lütfen şifrenizi giriniz")
    sifre= input("Şifreniz:")
    if sifre== banka['Sifre']:
        print("Doğru şifre girdiniz")
        print(f"{banka['Banka']} bankasında bulunan bakiyeniz:{banka['Bakiye']} tl'dir")
        print("""Yapmak istediğiniz işlemi seçin
                   1 - Para Çekme
                   2 - Para Yatırma
                   """)
        secim2=input("yapmak istediğiniz işlemi seçin:")
        if secim2=="1":
            cekilecek_tutar=float(input("çekmek istediğiniz miktarı giriniz:"))
            if cekilecek_tutar<=banka['Bakiye']:
                banka['Bakiye']-=cekilecek_tutar
                print(f"Hesabınızın yeni bakiyesi {banka['Bakiye']} tl'dir")
            elif cekilecek_tutar>banka['Bakiye']:
                print("Bakiyenizden fazlasını çekemezssiniz")
        elif secim2=="2":
            yatırılacak_miktar=float(input("yatırmak istediğiniz miktarı giriniz:"))
            banka['Bakiye']+=yatırılacak_miktar
            print(f"Hesabanızın yeni bakiyesi {banka['Bakiye']} tl'dir")


    else:
        while hak>1:
            hak-=1
            print(f"yanlış şifre girdiniz {hak} hakkınız kalmıştır dikkatli kullanın")
            secim3=input("Tekrar şifre girin:")
            if secim3 == "1":
                cekilecek_tutar = float(input("çekmek istediğiniz miktarı giriniz:"))
                if cekilecek_tutar <= banka['Bakiye']:
                    banka['Bakiye'] -= cekilecek_tutar
                    print(f"Hesabınızın yeni bakiyesi {banka['Bakiye']} tl'dir")
                elif cekilecek_tutar > banka['Bakiye']:
                    print("Bakiyenizden fazlasını çekemezssiniz")
            elif secim3 == "2":
                yatırılacak_miktar = float(input("yatırmak istediğiniz miktarı giriniz:"))
                banka['Bakiye'] += yatırılacak_miktar
                print(f"Hesabanızın yeni bakiyesi {banka['Bakiye']} tl'dir")
            else:
                print("Geçersiz bir işlem girdiniz")
        else:
            print("Hakkınız doldu kartınız bloke olmuştur.")
