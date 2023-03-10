

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
flip_timer = 300

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)




#flashcard
try:
    data = pandas.read_csv("flash-card-project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("flash-card-project/data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



# next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

# flip card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

#remove correct words
def save_words():
#remove correct words
    to_learn.remove(current_card)
    
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("flash-card-project-start/data/german_words.csv", index=False)
    next_card()

# UI
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title=canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word=canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_img = PhotoImage(file="flash-card-project-start/images/right.png")
wrong_img = PhotoImage(file="flash-card-project-start/images/wrong.png")
right_button = Button(image=right_img, highlightthickness=0, command= save_words)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()
