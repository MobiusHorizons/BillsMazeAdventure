import tkinter as tk
import random


terrains = ['dirt', 'stone']
map1 = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

class Map:
    def __init__(self, canvas):
        self.canvas = canvas
        self.load_tiles()
        self.config = map1
        self.objects = [];
        self.topleft = None
        self.width = 0
        self.height  = 0
        self.load_map()

    def load_tiles(self):
        self.tiles = {}
        for t in terrains:
            self.tiles[t] = tk.PhotoImage(file='./tiles/map-' + t + '.gif')

    def load_map(self):
        self.height = len(self.config) * 64
        self.width = len(self.config[0]) * 64

        for y, row in enumerate(self.config):
            for x, tile in enumerate(row):
                tile_image = self.tiles[terrains[tile]]
                canvas_tile = self.canvas.create_image(x * 64, y * 64, anchor=tk.NW, image=tile_image,tags=('terrain',terrains[tile]))
                if x == 0 and y == 0:
                    self.topleft = canvas_tile
                self.objects.append(canvas_tile);

    def coords(self):
        [x, y] = self.canvas.coords(self.topleft)
        return [-x, -y]

    def move(self, x, y):
        x = min(max(x, 0), self.width - self.canvas.winfo_width())
        y = min(max(y, 0), self.height - self.canvas.winfo_height())

        [currentX, currentY] = self.coords()
        print((x,y),(currentX,currentY))

        deltaX = (x - currentX)
        deltaY = (y - currentY)

        print((deltaX, deltaY))

        for obj in self.objects:
            self.canvas.move(obj, -1 * deltaX, -1 * deltaY)

        return self.coords()


