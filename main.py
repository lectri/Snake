import pyglet
from pyglet import shapes
from pyglet.window import key
from pyglet import clock
import config as c


# Create Window
window = pyglet.window.Window(c.width, c.height, caption=c.caption)

# Create Sprite & Batch
spriteBatch = pyglet.graphics.Batch()
snakeSprite = shapes.Rectangle(x=200, y=200, width=25, height=25, color=(152, 255, 152), batch=spriteBatch)

# Decorator Methods
@window.event
def on_draw():  
    window.clear()
    spriteBatch.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        c.snakeDirection = "L"
    if symbol == key.RIGHT:
        c.snakeDirection = "R"
    if symbol == key.UP:
        c.snakeDirection = "U"
    if symbol == key.DOWN:
        c.snakeDirection = "D"

# Other Methods
def move(dt):
    if c.snakeDirection == "L":
        snakeSprite.x -= 5
    if c.snakeDirection == "R":
        snakeSprite.x += 5
    if c.snakeDirection == "U":
        snakeSprite.y += 5
    if c.snakeDirection == "D":
        snakeSprite.y -= 5

# Run
pyglet.app.run()