BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

import tkinter
import pandas
import random


# Words
data = pandas.read_csv("day31/flash-card-project-start/data/french_words.csv")
data_dict = data.to_dict(orient="records")


def displayFrench():
    wordPair = random.choice(data_dict)
    print(wordPair['French'])
    card.itemconfig(flashWord, text=f"{wordPair['French']}")

# Create the UI
window = tkinter.Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Language Flash Cards")

# Add the flash card
cardFrontImg = tkinter.PhotoImage(file="day31/flash-card-project-start/images/card_front.png")
card = tkinter.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
flashCard = card.create_image(400, 263, image = cardFrontImg)
flashLang = card.create_text(400, 150, text="FRENCH", font=(FONT_NAME, 40, "italic") )
flashWord = card.create_text(400,263, text="", font=(FONT_NAME, 60, "bold"))
card.grid(column=0, row=0, columnspan=2)


tickImg = tkinter.PhotoImage(file="day31/flash-card-project-start/images/right.png")
tickButton = tkinter.Button(image=tickImg, background=BACKGROUND_COLOR, command=displayFrench)
tickButton.grid(column=1, row=1)

crossImg = tkinter.PhotoImage(file="day31/flash-card-project-start/images/wrong.png")
crossButton = tkinter.Button(image=crossImg, background=BACKGROUND_COLOR, command=displayFrench)
crossButton.grid(column=0, row=1)

window.mainloop()
