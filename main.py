import PIL
import pandas as pd
from tkinter import*
from tkinter import Tk, Button, Entry, Canvas
from PIL import ImageTk, Image

window=Tk()
window.title("Pokemonowy tekst")
image = Image.open('pokeball.png')
img=image.resize((200,200))
pic = PIL.ImageTk.PhotoImage(img)
canvas=Canvas(width=200, height=200,highlightthickness=0)
canvas.create_image(100,100,image=pic)
canvas.grid(column=1, row=1)
window.config(padx=20, pady=20)



df=pd.read_csv("pokemonowe_litery.csv")

df_dic={row.litera:row.znaczek for (index,row) in df.iterrows()}

#Entry word_entry
word_entry=Entry(width=45)

#UI setup
word_entry.grid(column=1, row=1)
word_entry.focus()


def poke_word():
    output_text =''
    word = word_entry.get()
    word=word.upper()
    for letter in word:
        if letter in df_dic:
            output_text=''.join([output_text, df_dic[letter]])
        else:
            output_text = ''.join([output_text,letter])

    word_entry.delete(0, 'end')
    word_entry.insert(0,output_text)




#button
button1=Button(text="Poke it!", width=10, command=poke_word)
button1.grid(column=1, row=2)
window.mainloop()