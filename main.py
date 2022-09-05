from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}
data_dict={}
# -------------------------------------- FILE READ -----------------------------------#
try:
    data_file = pandas.read_csv('data/unknown_word.csv')
except FileNotFoundError:
    data_file=pandas.read_csv('data/data.csv')
    data_dict=data_file.to_dict(orient='records')
else:
    data_dict = data_file.to_dict('records')



def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(data_dict)
    canvas.itemconfig(bangla_title, text="Bangla", fill="black")
    canvas.itemconfig(bangla_text, text=word["Bangla"], fill="black")
    canvas.itemconfig(card_background, image=img1)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(bangla_title, text="English", fill="white")
    canvas.itemconfig(bangla_text, text=word["English"], fill="white")
    canvas.itemconfig(card_background, image=img2)

def known_word():

    data_dict.remove(word)
    print(len(data_dict))
    data=pandas.DataFrame(data_dict)
    data.to_csv("data/unknown_word.csv",index=False)
    next_card()


# -------------------------------------- UI SETUP -----------------------------------#

window = Tk()
window.title("Bnagla Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)
# -------------------------------------- BANGLA UI-----------------------------------#
canvas = Canvas(width=800, height=526)
img1 = PhotoImage(file="./images/card_front.png")
img2 = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=img1)
bangla_title = canvas.create_text(400, 150, text="Bangla", font=("Ariel", 32, "italic"))
bangla_text = canvas.create_text(400, 263, text="Title", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# -------------------------------------- ENGLISH UI-----------------------------------#


right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=known_word)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()
window.mainloop()
