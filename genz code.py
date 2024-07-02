from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

windows=Tk()
windows.minsize(width=700,height=400)
windows.title("Password manager")
windows.config(padx=120,pady=70)

def generate_key():
    letters=["a","b","c","d","e","f","g","h","i","j","k","l"
             ,"m","n","o","p","q","r","s","t","u","v","w",
             "x","y","z"]
    numbers=["0","1","2","3","4","5","6","7","8","9"]
    symbols=["!","@","3","$","%","&","*","|"]
    password_letters=[choice(letters) for _ in range(randint(8,10))]
    password_numbers=[choice(numbers) for _ in range(randint(2,4))]
    password_symbols=[choice(symbols) for _ in range(randint(2,4))]

    password_list=password_letters+password_numbers+password_symbols
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure any entry shouln't be empty")
    else:
        is_ok=messagebox.askokcancel(title="website",message=f"Your website: {website} and password: {password} save successfully")


    if is_ok:
        with open("Pass_manager.txt","a") as data_file:
            data_file.write(f"{website}|{email}|{password}")
            website_entry.delete(0,END)
            password_entry.delete(0,END)


canvas=Canvas(width=210,height=220)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(110,120,image=logo_img)
canvas.grid(column=2,row=1)

#Label
website_label=Label(text="Website:")
website_label.grid(column=1,row=2)

email_label=Label(text="Email/Username:")
email_label.grid(column=1,row=3)

password_label=Label(text="Password:")
password_label.grid(column=1,row=4)

#Entry

website_entry=Entry(width=35)
website_entry.grid(column=2,row=2,columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(column=2,row=3,columnspan=2)
email_entry.insert(0,"reach2ayushgupta@gmail.com")


password_entry=Entry(width=21)
password_entry.grid(column=2,row=4)
#Button
add=Button(text="ADD",width=29,command=save)
add.grid(column=2,row=5,columnspan=2)

generate_password=Button(text="Generate Password",width=15,command=generate_key)
generate_password.grid(column=3,row=4)



windows.mainloop()