import pyautogui
import time
from tkinter import *


def start_spam():
    message = entryMessage.get()
    amount = int(entryAmount.get())
    time.sleep(5)

    while amount > 0:
        amount -= 1
        pyautogui.typewrite(message.strip())
        pyautogui.press('enter')


def extreme_mod():
    message = '!!! SPAM ATTACK IS ACTIVATED !!!'
    amount = 10
    time.sleep(5)

    while amount > 0:
        amount -= 1
        pyautogui.typewrite(message.strip())
        pyautogui.press('enter')
        amount += 1


window = Tk()
window.title('>>> SPAMER BY ITBERT <<<')
# window.iconbitmap('logo_spamer.ico')
window.resizable(width=False, height=False)
window.geometry('800x500')
window.config(bg='grey25')
window.config(cursor="star")

labelMain = Label()
labelMain.configure(
    text='Spamer by ITbert',
    fg='navajo white',
    bg='grey5',
    width=40,
    height=2,
    font='Arial 25',
    relief=RIDGE,
    borderwidth=7
)
labelMain.pack(expand=False, fill=NONE, side=TOP)


frameMain = Frame(borderwidth=7, relief=RIDGE, bg='grey5')

entryMessage = Entry(frameMain)
entryMessage.configure(
    justify=LEFT,
    state='normal',
    font='Arial 25',
    bg='grey5',
    fg='navajo white'
)
entryMessage.pack(anchor=NW, pady=20, padx=10)
entryMessage.focus()
entryMessage.insert(0, 'Текст (латиницей)')


entryAmount = Entry(frameMain)
entryAmount.configure(
    state='normal',
    font='Arial 25',
    bg='grey5',
    fg='navajo white'
)
entryAmount.pack(anchor=NW, pady=20, padx=10)
entryAmount.focus()
entryAmount.insert(2, 'Количество сообщений')


frameMain.pack(anchor=NW, pady=50, padx=10)


buttonEnter = Button()
buttonEnter.configure(
    justify=CENTER,
    text='НАЧАТЬ',
    font='Arial 25',
    width=10,
    height=2,
    relief=RIDGE,
    borderwidth=7,
    bg='grey5',
    fg='navajo white',
    activebackground='grey8',
    activeforeground='papaya whip',
    command=start_spam
)
buttonEnter.pack(side=LEFT, padx=10)


buttonExtreme = Button()
buttonExtreme.configure(
    justify=CENTER,
    text='EXTREME',
    font='Arial 25',
    width=12,
    height=2,
    relief=RIDGE,
    borderwidth=7,
    bg='grey5',
    fg='navajo white',
    activebackground='grey8',
    activeforeground='papaya whip',
    command=extreme_mod
)
buttonExtreme.pack(side=LEFT, padx=10, pady=10)


window.mainloop()
