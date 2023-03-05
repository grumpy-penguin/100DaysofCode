BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
wordPair = {}

import tkinter
import pandas
import random
from tkinter import messagebox


# Words
try:
    data = pandas.read_csv("day31/flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("day31/flash-card-project-start/data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")


def removeKnownWord(removeWord=False):
    # global wordPair
    if removeWord:
        data_dict.remove(wordPair)
    displayFrench()

def displayFrench():
    global wordPair, flip_timer
    window.after_cancel(flip_timer)
    wordPair = random.choice(data_dict)
    print(wordPair["French"])
    card.itemconfig(flashCard, image=cardFrontImg)
    card.itemconfig(flashLang, text="French", fill="black")
    card.itemconfig(flashWord, text=f"{wordPair['French']}", fill="black")
    window.after(3000, func=displayEnglish)

def displayEnglish():
    global wordPair
    card.itemconfig(flashCard, image=cardBackImg)
    card.itemconfig(flashLang, text="English", fill="white")
    card.itemconfig(flashWord, text=f"{wordPair['English']}", fill="white")

def saveWordsToLearn():
    if messagebox.askokcancel(title="Goodbye", message="Update dictionary based on this lesson?"):
        wordsDF = pandas.DataFrame(data_dict)
        wordsDF.to_csv("day31/flash-card-project-start/data/words_to_learn.csv", index=False)
    window.destroy()

# Create the UI
window = tkinter.Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Language Flash Cards")

flip_timer = window.after(3000, displayEnglish)
# Add the flash card
cardFrontImg = tkinter.PhotoImage(
    file="day31/flash-card-project-start/images/card_front.png"
)
cardBackImg = tkinter.PhotoImage(
    file="day31/flash-card-project-start/images/card_back.png"
)
card = tkinter.Canvas(
    width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR
)
flashCard = card.create_image(400, 263, image=cardFrontImg)
flashLang = card.create_text(400, 150, text="FRENCH", font=(FONT_NAME, 40, "italic"))
flashWord = card.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
card.grid(column=0, row=0, columnspan=2)


tickImg = tkinter.PhotoImage(file="day31/flash-card-project-start/images/right.png")
tickButton = tkinter.Button(
    image=tickImg, background=BACKGROUND_COLOR, command=lambda: removeKnownWord(removeWord=True)
)
tickButton.grid(column=1, row=1)

crossImg = tkinter.PhotoImage(file="day31/flash-card-project-start/images/wrong.png")
crossButton = tkinter.Button(
    image=crossImg, background=BACKGROUND_COLOR, command=lambda: removeKnownWord()
)
crossButton.grid(column=0, row=1)

displayFrench()

window.protocol("WM_DELETE_WINDOW", saveWordsToLearn)

window.mainloop()
