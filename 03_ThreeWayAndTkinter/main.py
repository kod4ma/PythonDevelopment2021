#!/usr/bin/env python3

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(1,weight=1)
        self.create_widgets()

    def create_widgets(self):
        F = tk.LabelFrame(self.master, text="frame", relief="groove")
        F.columnconfigure(0, weight=1)
        F.grid(sticky = 'new')

        F.newb = tk.Button(F)
        F.newb["text"] = "New"
        F.newb["command"] = self.do_new

        F.newb.grid(column=0, row=0)
        F.quit = tk.Button(F, text="Exit", 
                              command=self.master.destroy)
        F.quit.grid(column=1, row=0)  

        self.do_new()

    def do_new(self):
        print("hi!")



app = Application()
app.mainloop()