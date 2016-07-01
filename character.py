import tkinter as tk

class Character:
    def __init__(self, canvas, coords=[0,0]):
        self.canvas = canvas
        self.coords = coords

        self.images = {}
        self.load_images()

        self.facing = 'front'
        self.faces = {} 

        for face in ['right','back','left','front']:
            self.faces[face] = self.canvas.create_image(coords[0], coords[1], 
                    anchor=tk.NW, image=self.images[face], state=tk.HIDDEN);
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
        
        self.coords = [x,y]
        return self.coords

