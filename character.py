import tkinter as tk

class Character:
    def __init__(self, canvas, terrain, coords=[0,0]):
        self.canvas = canvas
        self._map = terrain

        self.coords = coords

        self.images = {}
        self.load_images()

        self.facing = 'front'
        self.faces = {} 
        
        screen_coords = self.screen_pos(coords)

        for face in ['right','back','left','front']:
            self.faces[face] = self.canvas.create_image(screen_coords[0], screen_coords[1], 
                    anchor=tk.NW, image=self.images[face], state=tk.HIDDEN);
        self.set_pos()
        self.face(self.facing);

    def load_images(self):
        self.images['front'] = tk.PhotoImage(file="./character/Bill-Front.gif");
        self.images['right'] = tk.PhotoImage(file="./character/Bill-Right.gif");
        self.images['back']  = tk.PhotoImage(file="./character/Bill-Back.gif");
        self.images['left']  = tk.PhotoImage(file="./character/Bill-Left.gif");

    def face(self, direction):
        for face in ['right', 'back', 'left', 'front']:
            self.canvas.itemconfig(self.faces[face], state=tk.HIDDEN)
        
        self.facing = direction
        self.canvas.itemconfig(self.faces[direction], state=tk.NORMAL)

    def move(self, direction):
        self.face(direction)
        # try to move
        [x, y] = self.coords
        
        if direction == 'front':
            y += 64;
        elif direction == 'back':
            y -=64
        elif direction == 'right':
            x += 64
        elif direction == 'left':
            x -= 64
        
        return self.set_pos([x,y])

    def screen_pos(self, coords=None, screen_dims=None):
        #calculate screen position
        if coords == None:
            coords = self.coords

        [sw,sh] = [0,0]
        if screen_dims == None:
            sw = self.canvas.winfo_width();
            sh = self.canvas.winfo_height();
        else:
            sw,sh = screen_dims
        
        mw = self._map.width
        mh = self._map.height

        gutterX = min(sw, self._map.width) / 2
        gutterY = min(sh, self._map.height) / 2

        [x,y] = coords
        [sx,sy] = [sw /2 , sh/2 ] 
        
        if (x < gutterX):
            sx -= (gutterX - x) 
        elif (x > (mw - gutterX)): 
            sx += (x - (mw - gutterX))

        if (y < gutterY):
            sy -= (gutterY - y)
        elif (y > (mh - gutterY)):
            sy += (y - (mh - gutterY))
        
        
        #sx = (sx//64)*64
        #sy = (sy//64) *64

        return [sx, sy]

    def set_pos(self, coords=None, screen_dims=None):
        oldcoords = self.coords

        if coords == None:
            coords = self.coords
        else:
            self.coords = coords

        if (not self._map.is_dirt(coords)):
            self.coords = oldcoords
            return oldcoords

        screen_coords = self.screen_pos(coords, screen_dims)

        for face in self.faces:
            self.canvas.coords(self.faces[face], screen_coords)

        self._map.move(coords[0], coords[1])

        return coords
