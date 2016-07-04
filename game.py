import map
import character

class Game():
    def __init__(self, canvas, width, height, won):
        self.width = width
        self.height = height
        self.canvas = canvas
        self.won = won

        self.init_map()
        self.init_character()
        
    def init_map(self):
        self._map = map.Map(self.canvas,  self.width, self.height)

    def init_character(self):
        self.character = character.Character(self.canvas, self._map, self._map.start)

    def set_pos(self, coords=None, screen_dims=None):
        self.character.set_pos(coords, screen_dims)

    def move(self, direction):
        position = self.character.move(direction)
        if self._map.end == position:
            self.canvas.after(1,self.won)
        return position

    def clean(self):
        self.character.clean()
        self._map.clean()

       
