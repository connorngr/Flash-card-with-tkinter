from enum import Flag
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
#pycharm


data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
global card
global flag
def next_card():
  global card, flag 
  flag = 0
  card = random.choice(to_learn)
  canvas.itemconfig(card_language, text="French")
  canvas.itemconfig(card_word, text=card["French"])
window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Flash card image
canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
f_canvas = canvas.create_image(400, 263, image=front_card)
card_language = canvas.create_text(400, 120, text="Title", font=("Arial", 40, "bold"))
card_word = canvas.create_text(400, 230, text="Word", font=("Arial", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
#Delete card
def flip_card():
  global card, flag
  if flag == 0:
    canvas.itemconfig(card_language, text="English")
    canvas.itemconfig(card_word, text=card["English"])
    canvas.itemconfig(f_canvas, image=back_card)
    flag = 1
  else:
    canvas.itemconfig(card_language, text="French")
    canvas.itemconfig(card_word, text=card["French"])
    canvas.itemconfig(f_canvas, image=front_card)
    flag = 0
  
canvas.tag_bind(f_canvas, '<Button-1>', lambda e:            
flip_card())

#buttons
#Create a function to move forgotten word to a new csv file: word_to_learn.csv
#Seach how to open file, handle exceptions
cross_image = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)
#Create the same function to save learned words, just in case
check_image = PhotoImage(file="images/right.png")
known_btn = Button(image=check_image, highlightthickness=0, command=next_card)
known_btn.grid(row=1, column=1)
#use try, catch exception to avoid program crash
next_card()
window.mainloop()
