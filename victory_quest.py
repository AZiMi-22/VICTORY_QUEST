import pyxel

class App:
    def __init__(self):
        self.counter = 0
        pyxel.init(160, 256)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): 
            self.counter += 1
    def draw(self):
        pyxel.cls(1)
        pyxel.text(10,10,f"score:{self.counter}",7)
App()
