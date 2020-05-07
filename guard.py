import pickle
import tkinter as tk
from tkinter import messagebox

guard = tk.Tk()
guard.geometry('500x150')
guard.title("Bot Guard")

tokenLabel = tk.LabelFrame(
    height=50, width=480, labelanchor = 'nw', text = 'token')
adminLabel = tk.LabelFrame(
    height=70, width=250, labelanchor = 'nw', text = "Owner's id")
btnLabel = tk.LabelFrame(
    height=62, width=220, labelanchor = 'nw', text = "")

token = tk.StringVar()
admin = tk.StringVar()

tokenEntry = tk.Entry(tokenLabel, width=64, textvariable=token)
adminEntry = tk.Entry(adminLabel, width=20, textvariable=admin)

Label_1 = tk.Label(adminLabel, text = "Ex: 123456789012345678 (the 18 digits)")
#label
tokenLabel.place(x=10, y=5)
adminLabel.place(x=10, y=60)
btnLabel.place(x=270, y=68)
#token
tokenEntry.place(x=10, y=5)
#admin
adminEntry.place(x=10, y=5)
Label_1.place(x=10, y=25)

def token_ok():
    global token
    #token = input("Entry the token \n>>> ")
    _token_ = str(token.get())
    if _token_ == '':
        messagebox.showinfo("info", "Entry can't be null")
        return False
    elif len(_token_) != 59:
        messagebox.showinfo("info", "Wrong type")
        return False
    else:
        theshell = open("servant.token","wb")
        #print(token)
        #print(type(token))
        #print(theshell)
        #print(type(theshell))
        pickle.dump(_token_, theshell)
        theshell.close()
        return True

def admin_ok():
    global admin
    owner = []
    i = admin.get()
    if i.isdigit() and len(str(i)) == 18:
        owner.append(int(i))
        theshell = open("admin.token","wb")
        pickle.dump(owner, theshell)
        theshell.close()
        return True
    else:
       messagebox.showinfo("info", "Wrong ID type")
       return False


def okandclose():
    a = admin_ok()
    b = token_ok()
    if a and b:
        guard.destroy()

btn1 = tk.Button(
    btnLabel, text = "token update", command = token_ok, width = 12, height=1)
btn2 = tk.Button(
    btnLabel, text = "admin update", command = admin_ok, width = 12, height=1)
btn3 = tk.Button(
    btnLabel, text = "OK", command = okandclose, width = 12, height=2)

btn1.place(x=10, y=2)
btn2.place(x=10, y=29)
btn3.place(x=115, y=8)

guard.mainloop()
