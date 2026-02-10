from tkinter import *
import pandas as pd
import random as rd
background_color = "#B1DDC6"

df = pd.read_csv("data\\french_words.csv")
data = df.to_dict(orient= "records")

def pick_word():
    random_dict = rd.choice(data)
    return random_dict["French"]

def next_cart():
    canvas.itemconfig(word_text, text = pick_word())


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= background_color)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images\\card_front.png")



canvas.create_image(0,0, image=card_front_img, anchor = "nw")
canvas.grid(row=0, column=0, columnspan= 2)
canvas.create_text(400,150, text="french" , font=("Ariel",40, "italic"))
word_text = canvas.create_text(400,263, text=pick_word()  , font=("Ariel",60, "bold"))

wrong_img = PhotoImage(file="images\\wrong.png")
button = Button(image=wrong_img, highlightthickness=0, command=next_cart)
button.grid(row=1, column=0)

right_img = PhotoImage(file="images\\right.png")
button = Button(image=right_img, highlightthickness=0, command= next_cart)
button.grid(row=1, column=1)





window.mainloop()