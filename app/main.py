from tkinter import *
from PIL import ImageTk, Image
from .prediction import prediction
import os

def launch_main_app():
    root = Tk()
    root.title("Stock Prediction")
    root.geometry("1500x1000")

    base_path = os.path.dirname(__file__)
    print(base_path)
    bg_path = os.path.join(base_path, 'assets/background.jpg')
    c = Canvas(root, width=1500, height=1000)
    bg_img = ImageTk.PhotoImage(Image.open(bg_path).resize((1500, 1000)))
    c.create_image(0, 0, image=bg_img, anchor='nw')
    c.pack(fill="both", expand=True)

    label = Label(c, text="STOCKS", font=('arial', 15, 'bold')).pack()

    stocks = [
        ("Google", 'google.png', 'GOOG.csv'),
        ("Facebook", 'facebook.png', 'FB.csv'),
        ("Twitter", 'twitter.png', 'TWTR.csv'),
        ("Microsoft", 'microsoft.png', 'MSFT.csv'),
        ("Tesla", 'tesla.png', 'TSLA.csv'),
        ("Apple", 'apple.png', 'APPLE.csv'),
        ("Amazon", 'amazon.png', 'AMZN.csv'),
    ]

    icons = []

    for i, (name, icon_file, data_file) in enumerate(stocks):
        icon = PhotoImage(file=os.path.join(base_path, 'assets', icon_file))
        icon = icon.subsample(2, 2)
        print(os.path.join(base_path, 'assets', icon_file))
        icons.append(icon)
        file_path = os.path.join(base_path, '..', 'data', data_file)
        btn = Button(root, text=name, font=('arial', 10, 'bold'), padx=30, pady=5, bd=5, image=icon,
                     compound=LEFT, activebackground='#78d6ff',
                     command=lambda f=file_path: prediction(f))
        c.create_window(535, 30 + i * 90, anchor="nw", window=btn)

    root.mainloop()
