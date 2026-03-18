import random
import tkinter
from tkinter import *
from functools import partial

def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, gameboard, l1, l2)
            button[i][j] = Button(game_board, bd = 5, command = get_t, height = 4, width = 8)
            button[i][j].grid(row = m, column = n)
    gameboard.mainloop()

def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")

    l1 = Button(game_board, text = "Player : X", width = 10)
    l1.grid(row = 1, column = 1)
    l2 = Button(game_board, text = "Computer : O", width = 10, state = DISABLED)
    l2.grid(row = 2, column = 1)
    gameboard_pc(game_board, l1, l2)    

def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")

    l1 = Button(game_board, text = "Player 1 : X", width = 10)
    l1.grid(row = 1, column = 1)
    l2 = Button(game_board, text = "Player 2 : O", width = 10, state = DISABLED)
    l2.grid(row = 2, column = 1)
    gameboard_pl(game_board, l1, l2)


def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)

    head = Button(menu, text = "---Welcome to Tic Tac Toe---", activeforeground = "red", activebackground = "yellow", bg = "red", fg = "yellow", width = 500, font = "summer", bd = 5)

    B1 = Button(menu, text = "Single Player", activeforeground = "red", activebackground = "yellow", bg = "red", fg = "yellow", width = 500, font = "summer", bd = 5, command = wpc)

    B2 = Button(menu, text = "Multi player", activeforeground = "red", activebackground = "yellow", bg = "red", fg = "yellow", width = 500, font = "summer", bd = 5, command = wpl)

    B3 = Button(menu, text = "Exit", activeforeground = "red", activebackground = "yellow", bg = "red", fg = "yellow", width = 500, font = "summer", bd = 5, command = menu.quit)

    head.pack(side = "top")
    B1.pack(side = "top")
    B2.pack(side = "top")
    B3.pack(side = "top")
    menu.mainloop()

if __name__ == "__main__":
    play()
