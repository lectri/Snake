import pyglet
from pyglet import shapes
from pyglet.window import key
from pyglet import clock
import config as c
# Snake Variables/Constant
snakeDirection = ""

# Create Window
window = pyglet.window.Window(c.width, c.height, caption=c.caption)

# Create sprite batches
spriteBatch = pyglet.graphics.Batch()
sprite = shapes.Rectangle(x=200, y=200, width=25, height=25, color=(152, 255, 152), batch=spriteBatch)

# Decorator Methods
@window.event
def on_draw():  
    window.clear()
    spriteBatch.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        snakeDirection = "U"
    elif symbol == key.DOWN:
        snakeDirection = "D"
    elif symbol == key.LEFT:
        snakeDirection = "L"
    elif symbol == key.RIGHT:
        snakeDirection = "R"
    else:
        return None
        

# Sprite Movement Per Frame
def move(dt):
    if snakeDirection == "U":
        sprite.y += 5
    elif snakeDirection == "D":
        sprite.y -= 5
    elif snakeDirection == "L":
        sprite.x -= 5
    elif snakeDirection == "R":
        sprite.x += 5

# Scheduled Events
clock.schedule_interval_soft(move, 1/30)


# Run
pyglet.app.run()