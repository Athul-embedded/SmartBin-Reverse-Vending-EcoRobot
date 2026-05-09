from tkinter import *

root = Tk()

root.title("SmartBin Login")
root.geometry("400x300")

Label(root, text="SmartBin Login", font=("Arial", 18)).pack(pady=20)

Label(root, text="Username").pack()
username = Entry(root)
username.pack()

Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

Button(root, text="Login").pack(pady=20)

root.mainloop()
