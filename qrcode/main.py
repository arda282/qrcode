import customtkinter #tkinterin duzenlenmis bir modulu
from PIL import Image
import os


root = customtkinter.CTk() #penceremizi olusturuyoruz

root.title("QR code olusturucu") #penceremizin basligi

def button1(): #butonlarin fonksiyonlarini ayarliyoruz
    pass

def qrcode_generate():
    import qrcode

    def demo():
        text = qrcode_entry.get()
        img = qrcode.make(text)
        img.save("qr.png")
        open = Image.open("qr.png")

    demo()

frame_1 = customtkinter.CTkFrame(master=root) # cerceveleri olusturalim
frame_1.place(relx=0.1,rely=0.1, relwidth=0.8,relheight=0.8)

button_1 = customtkinter.CTkButton(master=frame_1, text="Press me", command=button1) #cerceve uzerindeki elementleri olusturuyouz
button_1.place(relx=0.45,rely=0.05)

button_2 = customtkinter.CTkButton(master=frame_1, text="QR Kod olusturucu", command=qrcode_generate) #QR kode olusturucu butonu
button_2.place(relx=0.45,rely=0.05)

qrcode_entry = customtkinter.CTkEntry(master=frame_1) #QR kode olusturucu yazisi
qrcode_entry.place(relx=0.45,rely=0.1)

root.mainloop() #pencere kapatilana kadar acik kalmasini sagliyoruz