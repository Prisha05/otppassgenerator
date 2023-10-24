from tkinter import *
from tkinter.filedialog import asksaveasfile
import random

root = Tk()
root.title("Password & OTP Generator")
root.geometry("600x680")
root.configure(bg='firebrick4')

def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())
    my_password = ' '
    for _ in range(pw_length):
        my_password += chr(random.randint(33, 126))
    pw_entry.insert(0, my_password)

def new_rand1():
    OTP_entry.delete(0, END)
    my_otp = str(random.randint(1000, 9999))
    OTP_entry.insert(0, my_otp)

def save():
    files = [('All Files', '.'), ('Python Files', '*.py'), ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes=files, defaultextension=files)
    if file:
        password_info = pw_entry.get()
        otp_info = OTP_entry.get()
        file.write("\nYour General Password is - " + password_info)
        file.write("\nYour OTP is - " + otp_info)
        file.close()

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

def clipper1():
    root.clipboard_clear()
    root.clipboard_append(OTP_entry.get())

lf = LabelFrame(root, text="Password Length", bg='gainsboro', font=('Spectral', 11))
lf.pack(pady=20)

my_entry = Entry(lf, bg='rosybrown1', font=("helvetica", 27))
my_entry.pack(pady=20, padx=20)

lf1 = LabelFrame(root, text="Password", bg='gainsboro', font=('Spectral', 11))
lf1.pack(pady=20)

pw_entry = Entry(lf1, text='', bg='rosybrown1', font=("helvetica", 27))
pw_entry.pack(padx=20, pady=20)

o = LabelFrame(root, text="OTP", bg='gainsboro', font=('Spectral', 11))
o.pack(pady=40)

OTP_entry = Entry(o, text='', bg="rosybrown1", font=("helvetica", 27))
OTP_entry.pack(pady=20, padx=20)

my_frame = Frame(root, bg='firebrick4')
my_frame.pack(pady=20)

my_button = Button(my_frame, bg='khaki3', text="Generate Strong Password", command=new_rand, bd=3)
my_button.grid(row=0, column=0, padx=10)

my_button = Button(my_frame, bg="khaki3", text="Generate OTP", command=new_rand1, bd=3)
my_button.grid(row=0, column=1, padx=10)

my_frame1 = Frame(root, bg='firebrick4')
my_frame1.pack(pady=10)

clip_button = Button(my_frame1, bg="burlywood1", text="Copy To clipboard", command=clipper, bd=3)
clip_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame1, bg='burlywood1', text="Copy To clipboard", command=clipper1, bd=3)
clip_button.grid(row=0, column=1, padx=10)

my_frame2 = Frame(root, bg='firebrick4')
my_frame2.pack(pady=20)

save_button = Button(my_frame2, bg='burlywood1', text="Save", command=save, bd=3)
save_button.grid(row=0, column=0)

root.mainloop()
