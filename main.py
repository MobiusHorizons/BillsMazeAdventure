#!/usr/local/bin/python3

import tkinter as tk
import game

class Application(tk.Frame):
    def __init__(self, master=None):
        self.coords = [0,0]
        tk.Frame.__init__(self, master)
        self.config(padx=0, pady=0)
        self.TK = self.master
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.init_canvas()
        self.init_game()
        self.init_events()

    def init_canvas(self):
        self.canvas = tk.Canvas(self)
        self.canvas.configure(background='black')
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

    def init_game(self):
        self.game_width = 5
        self.game_height = 5
        def new_game():
            self.game_width = self.game_width + 5
            self.game_height = self.game_height + 5
            self.game = game.Game(self.canvas, self.game_width, self.game_height, new_game)

        self.game= game.Game(self.canvas, self.game_width, self.game_height, new_game)
        
    def init_events(self):
        self.TK.bind('<Right>', self.right)
        self.TK.bind('<Left>', self.left)
        self.TK.bind('<Up>', self.up)
        self.TK.bind('<Down>', self.down)
        self.TK.bind("f", self.fullscreen(True)) 
        self.TK.bind("<Escape>", self.fullscreen(False)) 
        self.canvas.bind("<Configure>", self.resize)

    def fullscreen(self, value):
        def set_fullscreen(event):
            self.TK.attributes("-fullscreen", value)
        return set_fullscreen

    def resize(self, event):
        w,h = event.width, event.height
        self.game.set_pos(screen_dims=[w,h])

    def up(self, event):
        self.coords = self.game.move('back')

    def down(self, event):
        self.coords = self.game.move('front')

    def left(self, event):
        self.coords =self.game.move('left')

    def right(self, event):
        self.coords = self.game.move('right')



app = Application()
app.master.title('Sample')
app.mainloop()
