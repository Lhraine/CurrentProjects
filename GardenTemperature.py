_author_ = "Jessika Strum"
#importing tkinter
from tkinter import*
from tkinter import messagebox

root = Tk()
root.title('Garden Temperature Reader')
root.configure(bg='#ffe5b4')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("350x220")

def number():
    try:
        int(my_box.get())
        answer.config(text="The plants are okay.")
    except ValueError:
           answer.config(text="The plants are cold. Bring them inside.")


my_label= Label(root, text="What is the temperature?", bg='#ffe5b4')
my_label.pack(pady=20)

my_box = Entry(root, bg='#ffffff')
my_box.pack(pady=10)

my_button = Button(root, bg='#ffffff', text="Submit", command=number)
my_button.pack(pady=5)

answer = Label(root, text='', bg='#ffe5b4')
answer.pack(pady=20)
   #if num <= 15:
       #print("Plants are cold")
   #else:
   # print("The plants are okay")

root.mainloop()



