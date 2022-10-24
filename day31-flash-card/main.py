from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
# Read data from csv

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")
current_card = {}

# button functions
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    current_word  = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill='green')
    canvas.itemconfig(card_word,text=current_word, fill='green')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)
    
def is_known():
    word_list.remove(current_card)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# UI Stuff
window = Tk()
window.title("FlashCardz")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title =canvas.create_text(400,150,text='Title',font=("Arial",40,"italic"))
card_word  = canvas.create_text(400, 263, text='word', font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file='images/right.png')
unknown_button = Button(image=check_image, command=is_known)
unknown_button.grid(row=1,column=1)


next_card()
window.mainloop()