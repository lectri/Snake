import random
import pyglet
from pyglet import shapes
from pyglet.window import key
from pyglet import clock
import config as c


# Create Window
window = pyglet.window.Window(c.WIDTH, c.HEIGHT, caption=c.caption)

# Create Sprite Setup & Batch
sprite_batch = pyglet.graphics.Batch()
snake_sprite = shapes.Rectangle(x=200, y=200, width=25, height=25, color=(152, 255, 152), batch=sprite_batch)
apple_sprite = shapes.Rectangle(x=random.randint(1, c.WIDTH), y=random.randint(1, c.HEIGHT), width=25, height=25, color=(255, 0, 0), batch=sprite_batch)

# Decorator Methods
@window.event
def on_draw():  
    window.clear()
    sprite_batch.draw()
    

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        c.snake_direction = "L"
    if symbol == key.RIGHT:
        c.snake_direction = "R"
    if symbol == key.UP:
        c.snake_direction = "U"
    if symbol == key.DOWN:
        c.snake_direction = "D"

# Other Methods
def move(dt):
    if c.snake_direction == "L":
        snake_sprite.x -= 5
    if c.snake_direction == "R":
        snake_sprite.x += 5
    if c.snake_direction == "U":
        snake_sprite.y += 5
    if c.snake_direction == "D":
        snake_sprite.y -= 5

def collison_check(dt, sprite, target):
    # If the check reaches 4, there's a collision; returns true.
    check = 0
    if target.x < sprite.x + target.width:
        check += 1
    if target.x + target.width > sprite.x:
        check += 1
    if target.y < sprite.y + sprite.height:
        check += 1
    if target.y + target.height > sprite.y:
        check += 1
    
    if check == 4:
        apple_snake_collide_handle()

# Collision Handle: Change Apple Position
def apple_snake_collide_handle():
    global apple_sprite
    apple_sprite.x = random.randint(1, c.WIDTH)
    apple_sprite.y = random.randint(1, c.HEIGHT)

# NEXT UP: CREATE A FUNCTION THAT CHANGES THE PLAYERS POSTION DEPENDING ON THE SNAKEDIRECTION STRING. THEN MAKE IT A FUNCTION THAT GETS CALLED 60 TIMES A SECOND
pyglet.clock.schedule_interval_soft(move, 1/60)
pyglet.clock.schedule_interval_soft(collison_check, 1/60, snake_sprite, apple_sprite)


# Run
if __name__ == "__main__":
    pyglet.app.run()