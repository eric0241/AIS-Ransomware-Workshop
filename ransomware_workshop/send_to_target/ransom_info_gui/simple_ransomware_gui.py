import tkinter as tk
from tkinter import *
import time


root = tk.Tk()
root.title("YOU HAVE BEEN HACKED")
root.geometry("1250x450")


info_label = Label(root,
					text="Hello! Your computer has been compromised by ransomware.\n\nPlease follow the below instructions to regain acces to your files.\n\nANY ATTEMPT TO BYPASS THE INSTRUCTIONS WILL RESULT IN THE DELETION OF THE DECRYPTION KEY.",
					bg="red",
					# width=10,
					# height=400
					)
info_label.config(font=("Courier", 20))
info_label.grid(row=0, column=1)


instruction_label = Label(root, anchor="w", text="\n\n\nSend 0.5 BTC to the following address: ........................")
instruction_label.config(font=("Courier", 20))
instruction_label.grid(row=1, column=1)





def check_if_payment_sent():
	pass


root.mainloop()