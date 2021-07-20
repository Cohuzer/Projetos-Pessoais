from tkinter import *

app = Tk()

app.title("Cohuzer")
app.geometry("500x300")
app.config(background="#008")

txt1 = Label(app, text="Cohuzer", background="#ff0", foreground="#000")
txt1.place(x=10, y=10, width=150, height=50)

app.mainloop()
