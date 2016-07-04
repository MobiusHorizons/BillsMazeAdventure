#!/usr/local/bin/python3

import tkinter as tk
from tkinter import messagebox
import game

class Application(tk.Frame):
    def __init__(self, master=None):
        self.coords = [0,0]
        tk.Frame.__init__(self, master)
        self.config(padx=0, pady=0)
        self.master.minsize(width=640, height=480)
        self.TK = self.master
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.init_canvas()
        self.init_game()
        self.init_events()

    def init_canvas(self):
        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.canvas.configure(background='black')
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

    def init_game(self):
        self.game_width = 5
        self.game_height = 5
        def new_game():
            title = "You beat level %d!!" % (self.game_height // 5)
            message = "%s\nWould you like to continue to the next level?" % (title)
            if (messagebox.askyesno(title, message)):
                self.game_width = self.game_width + 5
                self.game_height = self.game_height + 5
                self.game.clean()
                self.game = game.Game(self.canvas, self.game_width, self.game_height, new_game)
            else :
                self.TK.destroy()

        self.game= game.Game(self.canvas, self.game_width, self.game_height, new_game)
        
    def init_events(self):
        self.moving = False
        # navigation
        self.TK.bind('<Right>', self.keydown('right'))
        self.TK.bind('<Left>', self.keydown('left'))
        self.TK.bind('<Up>', self.keydown('back'))
        self.TK.bind('<Down>', self.keydown('front'))

        # UI
        self.TK.bind("f", self.fullscreen(True)) 
        self.TK.bind("<Escape>", self.fullscreen(False)) 
        self.TK.bind("q", self.ask_quit)

        #Resizing
        self.canvas.bind("<Configure>", self.resize)

    def fullscreen(self, value):
        def set_fullscreen(event):
            self.TK.attributes("-fullscreen", value)
        return set_fullscreen

    def resize(self, event):
        w,h = event.width, event.height
        self.game.set_pos(screen_dims=[w,h])

    def ask_quit(self, event):
        if (messagebox.askokcancel("Quit","Are you sure you want to quit?")):
            self.TK.destroy()
    
    def animate_move(self, direction):
        if (self.moving):
            self.coords = self.game.move(direction)
            self.moving = False

    def keydown(self, direction):

        def handler(event):
            if self.moving:
                #debounce navigation
                return
            self.moving = True
            coords = self.game.move(direction)
            if (coords == self.coords):
                self.moving = False
            else:
                self.coords = coords
                self.canvas.after(35, self.animate_move, direction)

        return handler

app = Application()
app.master.title('Bill\'s Maze Adventure')
app.mainloop()
