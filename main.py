import time
import pyglet
from pyglet import shapes
from pyglet.window import key
from pyglet import clock
import config as c

# Sprite Direction
snakeDirection = ""

# Create Window
window = pyglet.window.Window(c.width, c.height, caption=c.caption)

# Create sprite batches
spriteBatch = pyglet.graphics.Batch()
snakeSprite = shapes.Rectangle(x=200, y=200, width=25, height=25, color=(152, 255, 152), batch=spriteBatch)




# Decorator Methods
@window.event
def on_draw():
    window.clear()
    spriteBatch.draw()

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.LEFT:
        snakeDirection = "Left"
    if symbol == key.RIGHT:
        snakeDirection = "Right"
    if symbol == key.UP:
        snakeDirection = "Up"
    if symbol == key.DOWN:
        snakeDirection = "Down"
    
# NEXT UP: CREATE A FUNCTION THAT CHANGES THE PLAYERS POSTION DEPENDING ON THE SNAKEDIRECTION STRING. THEN MAKE IT A FUNCTION THAT GETS CALLED 60 TIMES A SECOND
def move(dt):
    if snakeDirection == "Left":
        snakeSprite.x -= 5
    if snakeDirection == "Right":
        snakeSprite.x += 5
    if snakeDirection == "Up":
        snakeSprite.y += 5
    if snakeDirection == "Down":
        snakeSprite.y -= 5


pyglet.clock.schedule_interval(move, 1/30)


# Run
pyglet.app.run()