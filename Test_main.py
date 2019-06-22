from tkinter import *
total = 0
def submit():
    global total
    total = Textentry.get()
    output.delete(0.0,END)

window = Tk()
window.title=("New Game")
window.configure(background="white")

say= Label(window, text="Hi, we are starting a game")
say.pack()
say1=Label(window, text="Welcome to NIM!")
say1.pack()
say2=Label(window, text="How many balls do you want to get?")
say2.pack()

Textentry = Entry(window)
Button(window, text="SUBMIT")

output = Text(window, wrap=WORD)
window.mainloop()
