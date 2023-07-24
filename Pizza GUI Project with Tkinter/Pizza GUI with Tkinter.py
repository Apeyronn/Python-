from tkinter import *
from PIL import Image, ImageTk
import os

# Define the kullanıcı_sözlük dictionary
kullanıcı_sözlük = [
    {"Kullanıcı": "e", "Şifre": "1", "Bakiye": 100},
    {"Kullanıcı": "Veli", "Şifre": "12", "Bakiye": 120}
]

from tkinter import *
from PIL import Image, ImageTk
import os
import json

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Giriş Sayfası")
        self.root.geometry("350x475")

        self.image_path = "pizza_1.jpg"
        self.image = Image.open(self.image_path)
        self.image = self.image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = Label(root, text="Pizzaaaaaa", font=("Calibri"))
        self.image_label.pack(pady=20)

        self.Pizza_photo = Label(root, image=self.photo)
        self.Pizza_photo.pack()

        self.label1 = Label(root, text="Kullanıcı Adı", pady=20)
        self.label1.pack()
        self.entry1 = Entry(root)
        self.entry1.pack()

        self.label2 = Label(root, text="Şifre")
        self.label2.pack()
        self.entry2 = Entry(root)
        self.entry2.pack()

        self.Buton1 = Button(root, text="Giriş", command=self.check_login)
        self.Buton1.pack()

        self.label3 = Label(root, text="Kayıtlı Değil Misiniz? Buraya tıklayarak kayıt olun")
        self.label3.pack(pady=15)

        self.Buton2 = Button(root, text="Kayıt sayfasına git", command=self.open_register_page)
        self.Buton2.pack()

    def check_login(self):
        kullanıcı_adı = self.entry1.get()
        şifre = self.entry2.get()

        for index, kullanıcı in enumerate(kullanıcı_sözlük):
            if kullanıcı_adı == kullanıcı["Kullanıcı"] and şifre == kullanıcı["Şifre"]:
                self.open_pizza_page(index)
                break

    def open_register_page(self):
        self.register_page = Toplevel(self.root)
        self.register_app = RegisterPage(self.register_page)

    def open_pizza_page(self, selected_user_index):
        self.pizza_page = Toplevel(self.root)
        self.pizza_app = PizzaPage(self.pizza_page, selected_user_index)

class RegisterPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Kayıt Sayfası")
        self.root.geometry("350x350")

        self.label1 = Label(root, text="Kullanıcı Adı", pady=20)
        self.label1.pack()
        self.entry1 = Entry(root)
        self.entry1.pack()

        self.label2 = Label(root, text="Şifre")
        self.label2.pack()
        self.entry2 = Entry(root)
        self.entry2.pack()

        self.label3 = Label(root, text="Bakiye")
        self.label3.pack()
        self.entry3 = Entry(root)
        self.entry3.pack()

        self.Buton1 = Button(root, text="Kayıt Ol", command=self.register_user)
        self.Buton1.pack()

    def register_user(self):
        kullanıcı_adı = self.entry1.get()
        şifre = self.entry2.get()
        bakiye = float(self.entry3.get())

        new_user = {"Kullanıcı": kullanıcı_adı, "Şifre": şifre, "Bakiye": bakiye}
        kullanıcı_sözlük.append(new_user)
        self.save_data()
        self.root.destroy()

    def save_data(self):
        with open("data.json", "w") as file:
            json.dump(kullanıcı_sözlük, file)

class PizzaPage:
    def __init__(self, root, selected_user_index):
        self.root = root
        self.root.title("Pizzanızı Seçiniz")
        self.root.geometry("500x650")

        self.selected_user_index = selected_user_index

        self.label = Label(self.root, text="Pizzanızı Seçiniz", font=("Calibri", 16))
        self.label.pack(pady=20)

        self.image_folder_path = r"C:\Users\erdem\OneDrive\Masaüstü\Pizza"
        self.image_files = os.listdir(self.image_folder_path)

        self.pizza_info = [
            {"name": "Klasik Pizza", "price": "45 TL"},
            {"name": "Mantarlı Pizza", "price": "50 TL"},
            {"name": "Sucuklu Pizza", "price": "55 TL"},
            {"name": "Kaşarlı Pizza", "price": "65 TL"},
            # Burada diğer pizza bilgilerini ekleyebilirsiniz
        ]

        self.selected_pizza = None
        self.selected_pizza_price = 0

        for i, image_file in enumerate(self.image_files):
            image_path = os.path.join(self.image_folder_path, image_file)
            image = Image.open(image_path)
            image = image.resize((80, 80))
            photo = ImageTk.PhotoImage(image)

            pizza_frame = Frame(self.root)
            pizza_frame.pack(pady=0)

            pizza_button = Button(pizza_frame, image=photo, command=lambda i=i: self.show_pizza_info(i))
            pizza_button.image = photo
            pizza_button.pack()

            pizza_name = Label(pizza_frame, text=self.pizza_info[i]["name"])
            pizza_name.pack()

            pizza_price = Label(pizza_frame, text=self.pizza_info[i]["price"])
            pizza_price.pack()

    def show_pizza_info(self, i):
        self.selected_pizza = self.pizza_info[i]["name"]
        self.selected_pizza_price = float(self.pizza_info[i]["price"].split()[0])

        pizza_info_page = Toplevel(self.root)
        pizza_info_page.title("Pizza Bilgileri")
        pizza_info_page.geometry("400x600")

        name_label = Label(pizza_info_page, text="Pizza Adı: " + self.pizza_info[i]["name"])
        name_label.pack()

        price_label = Label(pizza_info_page, text="Fiyatı: " + self.pizza_info[i]["price"])
        price_label.pack()

        soslar_sözlüğü = [
            {"Sos": "Zeytin", "Ücret": 1.5},
            {"Sos": "Mantarlar", "Ücret": 2.0},
            {"Sos": "Keçi Peyniri", "Ücret": 2.5},
            {"Sos": "Et", "Ücret": 3.0},
            {"Sos": "Soğan", "Ücret": 3.5},
            {"Sos": "Mısır", "Ücret": 4.0}
        ]

        self.image_folder_path = r"C:\Users\erdem\OneDrive\Masaüstü\Pizza\Soslar"
        self.image_files = os.listdir(self.image_folder_path)
        for i, image_file in enumerate(self.image_files):
            image_path = os.path.join(self.image_folder_path, image_file)
            image = Image.open(image_path)
            image = image.resize((80, 80))
            photo = ImageTk.PhotoImage(image)

            sos_frame = Frame(pizza_info_page)
            sos_frame.pack(pady=0)

            sos_button = Button(sos_frame, image=photo, command=lambda i=i: self.show_sos_info(i, soslar_sözlüğü))
            sos_button.image = photo
            sos_button.pack()

            sos_name = Label(sos_frame, text=soslar_sözlüğü[i]["Sos"])
            sos_name.pack()

            sos_price = Label(sos_frame, text="Ücret: " + str(soslar_sözlüğü[i]["Ücret"]) + " TL")
            sos_price.pack()

    def show_sos_info(self, i, soslar_sözlüğü):
        sos_info_page = Toplevel(self.root)
        sos_info_page.title("Sos Bilgileri")
        sos_info_page.geometry("300x200")

        name_pizza_label = Label(sos_info_page, text="Pizza Adı: " + self.pizza_info[i]["name"])
        name_pizza_label.pack()

        name_label = Label(sos_info_page, text="Sos Adı: " + soslar_sözlüğü[i]["Sos"])
        name_label.pack()

        price_label = Label(sos_info_page, text="Ücret: " + str(soslar_sözlüğü[i]["Ücret"]) + " TL")
        price_label.pack()

        # Calculate and display the total price including selected pizza and sauce
        total_price = self.selected_pizza_price + float(soslar_sözlüğü[i]["Ücret"])
        total_label = Label(sos_info_page, text="Toplam Ödenecek Ücret: " + str(total_price) + " TL")
        total_label.pack()

        # Calculate and display the remaining balance after the purchase
        remaining_balance = kullanıcı_sözlük[self.selected_user_index]["Bakiye"] - total_price
        balance_label = Label(sos_info_page, text="Hesapta Kalan Bakiye: " + str(remaining_balance) + " TL")
        balance_label.pack()


if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
    root.mainloop()
