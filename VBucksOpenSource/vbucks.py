from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import time

root = Tk()
root.geometry("350x250")
root.resizable(0,0)
root.title("Vbuck Client")

root.iconbitmap('./Imgs/OIP.ico')

def work():
    vbuck_btn.config(state="disabled")
    image2 = PhotoImage(file="./Imgs/youaregonnaregretthis.png")
    canvas.delete(itm)
    canvas.create_image(0, 0, anchor=tk.NW, image=image2)
    root.update()
    time.sleep(2)
    os.system("start microsoft.windows.camera:")
    root.destroy()
    
def if_closing():
     messagebox.showerror("HWO DARE U??", "YOU WILL NOT CLOSE THE CLIENT")
     

image1 = PhotoImage(file="./Imgs/used.png")

canvas = tk.Canvas(root, width=image1.width(), height=image1.height())
canvas.pack()

itm = canvas.create_image(0, 0, anchor=tk.NW, image=image1)

ico1 = PhotoImage(file='./Imgs/vbucks.png')

button_x = (canvas.winfo_reqwidth() - ico1.width()) // 2
button_y = (canvas.winfo_reqheight() - ico1.height()) // 2 + 40

vbuck_btn = Button(canvas, image=ico1, command=work, borderwidth=0, highlightthickness=0)
vbuck_btn.config(bg=canvas['bg'])
vbuck_btn.image = ico1
vbuck_btn.place(x=button_x, y=button_y)

canvas.create_image(button_x, button_y, anchor=tk.NW, image=ico1)

root.protocol("WM_DELETE_WINDOW", if_closing)
root.attributes("-toolwindow", 1)

root.mainloop()