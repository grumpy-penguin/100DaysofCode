import tkinter


def convert_to_km():
    miles = float(enter.get())
    km = round(miles * 1.609344)
    kmretlabel["text"] = f"{km}"


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

enter = tkinter.Entry(width=8)
enter.grid(column=1, row=0)

mlabel = tkinter.Label(text="Miles")
mlabel.grid(column=2, row=0)

islabel = tkinter.Label(text="is equal to")
islabel.grid(column=0, row=1)

kmretlabel = tkinter.Label(text="0")
kmretlabel.grid(column=1, row=1)

kmlabel = tkinter.Label(text="Km")
kmlabel.grid(column=2, row=1)

calculate = tkinter.Button(command=convert_to_km, text="Calculate")
calculate.grid(column=1, row=2)
window.mainloop()
