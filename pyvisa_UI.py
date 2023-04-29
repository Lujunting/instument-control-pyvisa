import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk

root = ctk.CTk()
root.title('keithley-2400 control window')
root.geometry('500x500')
img_path_1="save.png"
img_path_2="plot.png"

# def icon(img_path):
#     img = Image.open(img_path)
#     img = img.resize((15, 15))       # 縮小尺寸
#     icon = ImageTk.PhotoImage(img)   # 建立圖片物件
#     return icon

# menu = tk.Menu(root)
# menubar = tk.Menu(menu)
# menubar.add_command(label="Save", image=icon(img_path_1), compound='left')  # 加入圖片，圖片放在左邊
# menubar.add_command(label="Plot", image=icon(img_path_2), compound='left')
# menu.add_cascade(label='File', menu=menubar)

scrollable_frame=ctk.CTkScrollableFrame(root,width=300,height=300)
scrollable_frame.grid(column=0, row=0,ipadx=15,ipady=10)
# root.columnconfigure(0,weight=1)
# root.columnconfigure(1,weight=2)
btn_a = ctk.CTkButton(root, text='A',hover_color='blue')
btn_b = ctk.CTkButton(root, text='B')
btn_a.grid(column=0, row=0,ipadx=10,ipady=10)  # 放在 (0,0)
btn_b.grid(column=1, row=0,ipadx=10,ipady=10)  # 放在 (1,0)
# root.config(menu=menu)
root.mainloop()