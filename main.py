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
snake_sprite = shapes.Rectangle(
    x=200, y=200, width=25, height=25, color=(255, 255, 152), batch=sprite_batch)
apple_sprite = shapes.Rectangle(x=random.randint(250, c.WIDTH), y=random.randint(
    1, c.HEIGHT-100), width=25, height=25, color=(255, 0, 0), batch=sprite_batch)
sprite_list = [snake_sprite]

# Labels
score_label = pyglet.text.Label(
    f"Score = {c.LENGTH-1}",
    font_name="Roboto",
    font_size = 10,
    x=10, y=10
)

death_label = pyglet.text.Label(
    font_name="Roboto",
    font_size=25,
    x=c.WIDTH//2,
    y=c.HEIGHT//2,
    anchor_x = "center"
)
playing = True

# Decorator Methods
@window.event
def on_draw():
    global playing
    
    window.clear()
    if playing:
        score_label.draw()
        sprite_batch.draw()
    else:

        death_label.draw()
    

# Keyboard Input Sets Snake Direction
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

# Update
def update(dt):
    move()
    follow()
    out_of_bounds()
    snake_apple = collison_check(snake_sprite, apple_sprite)
    if snake_apple == True:
        apple_snake_handle()

# Non-Game Loop Functions
# Checks what snake direction the snake should be, and updates accordingly


def move():
    if c.snake_direction == "L":
        snake_sprite.x -= c.SPEED_RATE
    if c.snake_direction == "R":
        snake_sprite.x += c.SPEED_RATE
    if c.snake_direction == "U":
        snake_sprite.y += c.SPEED_RATE
    if c.snake_direction == "D":
        snake_sprite.y -= c.SPEED_RATE

# Checks for overlap between sprite and its target, if it meets criteria, check equals 4 and returns True


def collison_check(sprite, target):
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
        return True


def follow():
    global snake_sprite
    global sprite_list

    # Initalize pos with Head and Existing pos Parts
    pos = [[snake_sprite.x, snake_sprite.y]]
    sprites_len = len(sprite_list)
    for i in range(sprites_len):
        pos.append([sprite_list[i].x, sprite_list[i].y])

        # Take Positions of the last pos part and current
        last = pos[i - 1]
        current = pos[i]

        # Give Current Sprite Position the last snake position
        sprite_list[i].x = last[0]
        sprite_list[i].y = last[1]

    sprite_list[-1].visible = True
    return pos

# Collision Handle: Change Apple Position
def apple_snake_handle():
    apple_sprite.x = random.randint(100, c.WIDTH)
    apple_sprite.y = random.randint(1, c.HEIGHT-100)
    
    c.LENGTH += 1
    score_label.text = f"Score = {c.LENGTH-1}"

    for i in range(4):
        sprite_list.append(shapes.Rectangle(
            x=-100, y=-100, width=25, height=25, color=(152, 255, 152), batch=sprite_batch))

    
def out_of_bounds():
    if snake_sprite.x > c.WIDTH or snake_sprite.x < 0:
        kill()
    elif snake_sprite.y > c.HEIGHT or snake_sprite.y < 0:
        kill()

def kill():
    global snake_sprite, apple_sprite, sprite_list, score_label, playing
    playing = False
    pyglet.clock.unschedule(update) # Stop Updating Game

    snake_sprite.delete()
    apple_sprite.delete()

    del sprite_list
    
    window.clear()
    score_label.delete()

    death_label.text = f"You Died! Your score was {c.LENGTH-1}"

if playing:
    pyglet.clock.schedule_interval(update, 1/60)

# Run
if __name__ == "__main__":
    pyglet.app.run()