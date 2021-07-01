import snake
import pyglet
import handlers as h
from pyglet.window import key

class Window(snake.Game, pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self, 720, 480, "Snake")
        snake.Game.__init__(self)
        
        
        # Window Properties
        self.width = 720
        self.height = 480
        self.game_caption = "Snake"

        pyglet.clock.schedule_interval(self.should_restart, 1 / 60)
    
    def should_restart(self, dt):
        if self.restart == True:
            snake.Game.__init__(self)
      
    

if __name__ == '__main__':
    w = Window()
    pyglet.app.run()