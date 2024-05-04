import tkinter as tk
from tkinter import CENTER, END
import pyshorteners
def shorten():
    if shorty.get():
        shorty.delete(0,"end")
    if my_entry.get():
        #Convert to tiny url
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        shorty.insert("end",url)
root = tk.Tk()
root.title("Link shortener")
root.geometry("500x500")
my_label = tk.Label(root,text="Enter Link to short",font=("Arial",14))
my_label.pack(pady=20)
my_entry = tk.Entry(root,font=("Arial",14))
my_entry.pack(pady=20)
my_button = tk.Button(root,text="Shorten Link", command = shorten, font=("Arial",14))
my_button.pack(pady=20)
short_label = tk.Label(root,text="short Link",font=("Arial",14))
short_label.pack(pady=50)
shorty = tk.Entry(root,font=("Arial",14),justify=CENTER,width=30)
shorty.pack(pady=20)
root.mainloop()