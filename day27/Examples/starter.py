import tkinter

window = tkinter.Tk()
window.title("MY First GUI Progame")
window.minsize(600,600)

mylabel = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
mylabel.pack(side="left")

def button_clicked():
    mylabel["text"] = enter.get()

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()
enter = tkinter.Entry()
enter.pack()

# mylabel["text"] = enter.get()

window.mainloop()
