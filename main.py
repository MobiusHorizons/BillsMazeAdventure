#!/usr/local/bin/python3

import tkinter as tk
import map

class Application(tk.Frame):
    def __init__(self, master=None):
        self.coords = [0,0]
        tk.Frame.__init__(self, master)
        self.config(padx=0, pady=0)
        self.TK = self.master
        self.pack(fill=tk.BOTH, expand=tk.YES)
        #self.grid()
        #self.load_tiles()
        self.init_canvas()
        self.nav_step = 32
        self.init_events()

    def init_events(self):
        self.TK.bind('<Right>', self.right)
        self.TK.bind('<Left>', self.left)
        self.TK.bind('<Up>', self.up)
        self.TK.bind('<Down>', self.down)
        self.TK.bind("f", self.fullscreen(True)) 
        self.TK.bind("<Escape>", self.fullscreen(False)) 
        #self.bind("<Configure>", self.resize)

    def fullscreen(self, value):
        def set_fullscreen(event):
            self.TK.attributes("-fullscreen", value)
        return set_fullscreen

    def resize(self, event):
        w,h = event.width, event.height
        self.canvas.config(width=w, height=h)

    def load_tiles(self):
        self.images = {
                'dirt' : tk.PhotoImage(file="./tiles/map-dirt.gif"),
                'main-map' : tk.PhotoImage(file="./maps/Main-Map.gif"),
        }

    def init_canvas(self):
        self.canvas = tk.Canvas(self)
        self.canvas.configure(background='black')
        self.init_map()
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

    def init_map(self):
        self._map = map.Map(self.canvas)
        self._map.move(self.coords[0], self.coords[1]);
    
    def up(self, event):
        self.coords = self._map.move(self.coords[0], self.coords[1] - self.nav_step)
        print(self.coords)

    def down(self, event):
        self.coords = self._map.move(self.coords[0], self.coords[1] + self.nav_step)
        print(self.coords)

    def left(self, event):
        self.coords = self._map.move(self.coords[0] - self.nav_step, self.coords[1])
        print(self.coords)

    def right(self, event):
        self.coords = self._map.move(self.coords[0] + self.nav_step, self.coords[1])
        print(self.coords)



app = Application()
app.master.title('Sample')
app.mainloop()
