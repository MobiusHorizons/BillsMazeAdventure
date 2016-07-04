import tkinter as tk
import random
import os

import maze


terrains = ['dirt', 'stone', 'start', 'finish']

class Map:
    def __init__(self, canvas, width=5, height=5):
        self.canvas = canvas
        self.load_tiles()
        self.config = maze.make_maze(width, height)
        self.objects = [];
        self.topleft = None
        self.width = 64 * width
        self.height  = 64 * height
        self.load_map()
        self.start = [64, 0]
        self.end = [self.width - 128, self.height - 64]

    def load_tiles(self):
        self.tiles = {}
        resources = os.environ.get('RESOURCEPATH')
        if resources == None:
            resources = 'tiles/'
        for t in terrains:
            self.tiles[t] = tk.PhotoImage(file=os.path.join(resources, 'map-' + t + '.gif'))

    def load_map(self):
        self.height = len(self.config) * 64
        self.width = len(self.config[0]) * 64

        for y, row in enumerate(self.config):
            for x, tile in enumerate(row):
                tile_image = self.tiles[terrains[tile]]

                # if terrains[tile] == 'finish':
                    # self.end = [x *64, y *64]
                # elif terrains[tile] == 'start':
                    # self.start = [x * 64, y * 64]

                canvas_tile = self.canvas.create_image(x * 64, y * 64, anchor=tk.NW, image=tile_image,tags=('terrain',terrains[tile]))
                if x == 0 and y == 0:
                    self.topleft = canvas_tile
                self.objects.append(canvas_tile);

    def coords(self):
        [x, y] = self.canvas.coords(self.topleft)
        sw = self.canvas.winfo_width() ;
        sh = self.canvas.winfo_height();

        [x , y] = [-x, -y]

        x = (sw/2 ) + x
        y = (sh/2 ) + y

        return [x, y]

    def move(self, x, y):
        # set the position of the middle of the middle visible tile
        sw = self.canvas.winfo_width()   #screen width
        sh = self.canvas.winfo_height()  #screen height

        [mx, my] = x, y

        if (sw > self.width):
            mx = sw/2 - (sw - self.width)/2
        else:
            mx = min(max(x, sw/2), self.width  - sw/2)

        if (sh > self.height):
            my = sh/2 - (sh - self.height)/2
        else:
            my = min(max(y, sh/2), self.height - sh/2)

        #mx = (mx//64) * 64
        #my = (my//64) * 64

        [currentX, currentY] = self.coords()
        deltaX = (mx - currentX)
        deltaY = (my - currentY)

        for obj in self.objects:
            self.canvas.move(obj, -1 * deltaX, -1 * deltaY)

        return self.coords()

    def is_dirt(self, coords):
        # check if coords is solid
        [x,y] = coords
        x = round(x / 64)
        y = round(y / 64)
        return (
                 x >= 0 and x < len(self.config[0]) and
                 y >= 0 and y < len(self.config)    and 
                 self.config[y][x] != 1
               )

    def clean(self):
        #clean up map tiles
        for obj in self.objects:
            self.canvas.delete(obj)

