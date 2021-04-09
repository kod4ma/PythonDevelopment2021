#!/usr/bin/env python3

import tkinter as tk
import random
from functools import partial
from tkinter import messagebox as mb


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(1,weight=1)
        self.create_widgets()

    def create_widgets(self):
        F = tk.LabelFrame(self.master)
        F.columnconfigure(0, weight=1)
        F.grid(sticky = 'new')

        F.newb = tk.Button(F)
        F.newb["text"] = "New"
        F.newb["command"] = self.do_new

        F.newb.grid(column=0, row=0)
        F.quit = tk.Button(F, text="Exit", 
                              command=self.master.destroy)
        F.quit.grid(column=1, row=0)  

        self.G = tk.LabelFrame(self.master)
        self.G.grid()
        self.do_new()

    def do_new(self):
        self.G.grid_forget()
        self.G = tk.LabelFrame(self.master)
        for i in range(4):
            self.G.columnconfigure(i,weight=1)
            self.G.rowconfigure(i,weight=1)
        self.G.grid(sticky ='nsew')

        l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


        if (0): #change for easy win
            perm = [1,2,3,4,5,6,7,8,9,10,12,15,13,14,11]
        else:
            perm = sorted(l, key=lambda *args: random.random())

        self.G.newb = []
        self.G.newb_pos = []
        for i in range(0,15):
            self.G.newb.append(tk.Button(self.G, height = 2,  width = 3))
            self.G.newb_pos.append(i)
            self.G.newb[i]["text"] = perm[i]
            changexy = partial(self.change, i, i)
            self.G.newb[i]["command"] = changexy
            self.G.newb[i].grid(sticky = 'nsew',column=i%4, row=i//4)
        self.G.zero = 15

    def change(self, pos, ind):
        new_pos = self.G.zero
        if((pos//4 == new_pos//4 and abs(pos%4 - new_pos%4) == 1) or (pos%4 == new_pos%4 and abs(pos//4 - new_pos//4) == 1)):
            self.G.newb[ind].grid(sticky = 'nsew',column=self.G.zero%4, row=self.G.zero//4)
            changexy = partial(self.change, self.G.zero, ind)
            self.G.zero = pos
            self.G.newb[ind]["command"] = changexy
            self.G.newb_pos[ind] = new_pos
            self.win_test()

    def win_test(self):
        flag = True
        for i in  range(0,15):
            if(self.G.newb[i]["text"] != self.G.newb_pos[i] + 1 ):
                flag = False
        if flag:
            mb.showinfo(
            "Info",
            "Easy win!")
            self.do_new()





app = Application()
app.mainloop()