from tkinter import *
import pandas
import random

BACKGROUND_COLOR="#B1DDC6"
current_card = {}
all_words = {}

try:
    data=pandas.read_csv('data/words_i_dont_know.csv')

except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    all_words=original_data.to_dict(orient="records")

else:
    all_words=data.to_dict(orient="records")

  
def generate_word():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(all_words)
    canvas.itemconfig(title,text="French", fill="black")
    canvas.itemconfig(word,text=current_card["French"], fill='black')
    canvas.itemconfig(card_background,image=card_front)
    flip_timer = screen.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title,text="English", fill="white")
    canvas.itemconfig(word,text=current_card["English"], fill="white")
    canvas.itemconfig(card_background,image=card_back)

def if_know():
    all_words.remove(current_card)
    data=pandas.DataFrame(all_words)
    data.to_csv("data/words_i_dont_know.csv", index=False) #Dont add the index number to the newly created list
   
    generate_word()


screen = Tk()
screen.title("YOOO")
screen.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
flip_timer=screen.after(3000, func=flip_card)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

canvas = Canvas(bg="white", width=800, height=526)
card_background=canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

title=canvas.create_text(400, 150, text="", fill="black", font=("Courier", 40, "italic"))
word=canvas.create_text(400, 263, text="", fill="black", font=("Courier", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=if_know)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)


generate_word()



screen.mainloop()
