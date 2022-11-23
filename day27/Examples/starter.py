import tkinter


def button_clicked():
    mylabel["text"] = enter.get()


window = tkinter.Tk()
window.title("MY First GUI Progame")
window.minsize(600, 600)

mylabel = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
mylabel.grid(column=0, row=0)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

enter = tkinter.Entry()
enter.grid(column=3, row=2)

# mylabel["text"] = enter.get()

window.mainloop()
