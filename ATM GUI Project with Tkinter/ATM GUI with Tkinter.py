from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

bankalar = [
    {"Banka": "Denizbank", "Kullanıcı": "erdem1", "Bakiye": 3000, "Şifre": "1"},
    {"Banka": "Akbank", "Kullanıcı": "erdem12", "Bakiye": 6000, "Şifre": "12"},
    {"Banka": "Ziraat Bankası", "Kullanıcı": "erdem123", "Bakiye": 9000, "Şifre": "123"}
]
admin = {"Kullanıcı Adı": "admin", "Şifre": "admin"}
selected_bank = None
hak = 3


def select_bank(banka):
    global selected_bank
    selected_bank = next((b for b in bankalar if b["Banka"] == banka), None)
    if selected_bank:
        def Bank_info():
            bank_info = Toplevel(root)
            bank_info.title(selected_bank["Banka"] + " Bankası Giriş Ekranı")
            bank_info.geometry("300x200+500+300")

            label1 = Label(bank_info, text="Kullanıcı Adı")
            label1.pack()
            entry1 = Entry(bank_info)
            entry1.pack()

            label2 = Label(bank_info, text="Şifre")
            label2.pack()
            entry2 = Entry(bank_info, show="*")
            entry2.pack()

            def check_login():
                kullanici_adi = entry1.get()
                sifre = entry2.get()
                if sifre == selected_bank["Şifre"] and kullanici_adi == selected_bank['Kullanıcı']:
                    Bank_info_2()
                    bank_info.destroy()
                else:
                    global hak
                    hak -= 1
                    if hak > 0:
                        bilgi_label.config(text=f"Kullanıcı adınız veya şifreniz yanlıştır. [{hak} hakkınız kaldı.]")
                    else:
                        bilgi_label.config(text="Kartınız Bloke oldu")
                        root.after(3000, root.destroy)  # 3 saniye sonra otomatik olarak kapat

            login_button = Button(bank_info, text="Giriş", command=check_login)
            login_button.pack()

            # Bilgi mesajı için bir etiket oluşturun
            bilgi_label = Label(bank_info, text="")
            bilgi_label.pack()

        def Bank_info_2():
            bank_info_2 = Toplevel(root)
            bank_info_2.title(selected_bank["Banka"] + " Bankası Bilgileri")

            window_width = 300
            window_height = 300
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = int((screen_width / 2) - (window_width / 2))
            y = int((screen_height / 2) - (window_height / 2))
            bank_info_2.geometry(f"{window_width}x{window_height}+{x}+{y}")

            label3 = Label(bank_info_2, text="Kullanıcı: " + selected_bank["Kullanıcı"])
            label3.pack()

            label4 = Label(bank_info_2, text="Banka: " + selected_bank["Banka"])
            label4.pack()

            label5 = Label(bank_info_2, text="Bakiye: " + str(selected_bank["Bakiye"]))
            label5.pack()

            para_cek_label = Label(bank_info_2, text="Çekilecek Tutar:")
            para_cek_label.pack()
            cek_entry = Entry(bank_info_2)
            cek_entry.pack()

            def para_cek():
                cekilecek_tutar = float(cek_entry.get())
                if cekilecek_tutar <= selected_bank['Bakiye']:
                    selected_bank['Bakiye'] -= cekilecek_tutar
                    label5.config(text="Bakiye: " + str(selected_bank["Bakiye"]))
                else:
                    label5.config(text="Yetersiz bakiye.")

            para_cek_button = Button(bank_info_2, text="Para Çek", command=para_cek)
            para_cek_button.pack()

            para_yatir_label = Label(bank_info_2, text="Yatırılacak Miktar:")
            para_yatir_label.pack()
            yatir_entry = Entry(bank_info_2)
            yatir_entry.pack()

            def para_yatir():
                yatirilacak_miktar = float(yatir_entry.get())
                selected_bank['Bakiye'] += yatirilacak_miktar
                label5.config(text="Bakiye: " + str(selected_bank["Bakiye"]))

            para_yatir_button = Button(bank_info_2, text="Para Yatır", command=para_yatir)
            para_yatir_button.pack()

            main_back_button = Button(bank_info_2, text="Ana Sayfaya Dön", command=root.deiconify)
            main_back_button.pack()

        Bank_info()


def Bank_account():
    account_screen = Toplevel(root)
    account_screen.title("Banka Seç")
    account_screen.geometry("300x400+500+300")

    for banka in bankalar:
        banka_frame = Frame(account_screen)
        banka_frame.pack(pady=10)

        image_path = rf"C:\Users\erdem\OneDrive\Masaüstü\Atm\Atm_Bank_Account_İmage\{banka['Banka'].lower()}.png"

        image = Image.open(image_path)
        image = image.resize((50, 50))
        photo = ImageTk.PhotoImage(image)

        banka_button = Button(banka_frame, text=banka["Banka"], image=photo, compound=LEFT,
                              width=150, height=50, command=lambda b=banka["Banka"]: select_bank(b))

        banka_button.image = photo
        banka_button.pack()

    main_back_button = Button(account_screen, text="Ana Sayfaya Dön", command=root.deiconify)
    main_back_button.pack(pady=20)


def Bank_add():
    ekle_ekrani = Toplevel()
    ekle_ekrani.title("Yeni Banka Ekle")
    ekle_ekrani.geometry("300x250+500+300")

    label1 = Label(ekle_ekrani, text="Yeni banka adını giriniz:")
    label1.pack()

    banka_entry = Entry(ekle_ekrani)
    banka_entry.pack()

    label2 = Label(ekle_ekrani, text="Kullanıcı adını giriniz:")
    label2.pack()

    kullanici_entry = Entry(ekle_ekrani)
    kullanici_entry.pack()

    label3 = Label(ekle_ekrani, text="Hesap bakiyesini giriniz:")
    label3.pack()

    bakiye_entry = Entry(ekle_ekrani)
    bakiye_entry.pack()

    label4 = Label(ekle_ekrani, text="Şifreyi giriniz:")
    label4.pack()

    sifre_entry = Entry(ekle_ekrani, show="*")
    sifre_entry.pack()

    def banka_ekle():
        try:
            yeni_banka = {
                "Banka": banka_entry.get(),
                "Kullanıcı": kullanici_entry.get(),
                "Bakiye": float(bakiye_entry.get()),
                "Şifre": sifre_entry.get()
            }
            bankalar.append(yeni_banka)
            bilgi_label.config(text="Yeni banka başarıyla eklendi")
            ekle_ekrani.after(3000, ekle_ekrani.destroy)  # 3 saniye sonra otomatik olarak kapat

        except ValueError:
            error_label.config(text="Geçersiz bakiye değeri. Lütfen sayısal bir değer girin.")

    button = Button(ekle_ekrani, text="Ekle", command=banka_ekle)
    button.pack()

    error_label = Label(ekle_ekrani, text="", fg="red")
    error_label.pack()

    bilgi_label = Label(ekle_ekrani, text="", fg="green")
    bilgi_label.pack()


def Admin_Account():
    admin_ekrani = Toplevel()
    admin_ekrani.title("Admin Hesabı")
    admin_ekrani.geometry("300x200+500+300")

    label1 = Label(admin_ekrani, text="Kullanıcı Adı:")
    label1.pack()

    entry1 = Entry(admin_ekrani)
    entry1.pack()

    label2 = Label(admin_ekrani, text="Şifre:")
    label2.pack()

    entry2 = Entry(admin_ekrani, show="*")
    entry2.pack()

    def admin_login():
        kullanici_adi = entry1.get()
        sifre = entry2.get()
        if sifre == admin["Şifre"] and kullanici_adi == admin["Kullanıcı Adı"]:
            Admin_info()
            admin_ekrani.destroy()
        else:
            bilgi_label.config(text="Kullanıcı adı veya şifre yanlış.")

    login_button = Button(admin_ekrani, text="Giriş", command=admin_login)
    login_button.pack()

    bilgi_label = Label(admin_ekrani, text="")
    bilgi_label.pack()


def Admin_info():
    admin_info = Toplevel(root)
    admin_info.title("Admin Hesabı")
    admin_info.geometry("500x400+500+300")

    # Treeview oluşturun ve sütunları tanımlayın
    tree = ttk.Treeview(admin_info)
    tree["columns"] = ("Banka", "Kullanıcı", "Bakiye", "Şifre")

    # Sütunlar için başlıkları belirleyin
    tree.heading("Banka", text="Banka")
    tree.heading("Kullanıcı", text="Kullanıcı")
    tree.heading("Bakiye", text="Bakiye")
    tree.heading("Şifre", text="Şifre")

    # Sütun genişliklerini ayarlayın
    tree.column("Banka", width=100)
    tree.column("Kullanıcı", width=100)
    tree.column("Bakiye", width=100)
    tree.column("Şifre", width=100)

    # Bankalar sözlüğündeki her bir bilgiyi ağaç görünümüne ekleyin
    for banka in bankalar:
        tree.insert("", "end", text=banka["Banka"],
                    values=(banka["Banka"], banka["Kullanıcı"], banka["Bakiye"], banka["Şifre"]))

    # Ağaç görünümünü ekrana yerleştirin
    tree.pack(fill="both", expand=True)


root = Tk()
root.title("ATM Uygulaması")
root.geometry("300x450+500+300")

image_path = rf"C:\Users\erdem\OneDrive\Masaüstü\Atm\Ana_Sayfa\Bank.png"
image = Image.open(image_path)
image = image.resize((100, 100))
photo = ImageTk.PhotoImage(image)

label = Label(root, text="ATM Sistemine Hoş Geldiniz")
label.pack(pady=20)

# Resim için etiket oluşturun ve resmi etikete ayarlayın
image_label = Label(root, image=photo)
image_label.pack()

Banka_secme_butonu = Button(root, text="Banka Seç", font=("Calibri", 12), width=20, command=Bank_account)
Banka_secme_butonu.pack()

Banka_ekleme_butonu = Button(root, text="Banka Ekle", font=("Calibri", 12), width=20, command=Bank_add)
Banka_ekleme_butonu.pack()

Admin_Butonu = Button(root, text="Admin Girişi", font=("Calibri", 12), width=20, command=Admin_Account)
Admin_Butonu.pack()

root.mainloop()
