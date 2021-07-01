import random

import handlers as h
import pyglet
from pyglet.window import key


class Game:
    """
    A class that handles the window, and snake properties/functions.
    """
    def __init__(self, *args): # Constructor

        # Window Properties
        self.width = 720
        self.height = 480
        self.game_caption = "Snake"

        # Snake Properties
        self.direction = ""
        self.speed = 5
        self.length = 1
        self.alive = True
        self.head_color = (255, 105, 180)
        self.body_color = (0, 255, 152)

        # Game Properties 
        self.score_label = pyglet.text.Label(
                f"Score = {self.length - 1}",
                font_name="Roboto",
                font_size=10,
                x=10, y=10
        )
        self.death_label = pyglet.text.Label(
                font_name="Roboto",
                font_size=25,
                x=self.width // 2,
                y=self.height // 2,
                anchor_x="center"
        )
        self.retry_label = pyglet.text.Label("Press space to try again.",
                font_name="Roboto",
                font_size=20,
                x=(self.width // 2),
                y=(self.height // 2) - 40,
                anchor_x="center"
        )
        self.restart = False
        # Sprite Properties
        self.sprite_batch = pyglet.graphics.Batch()

        self.snake_sprite = pyglet.shapes.Rectangle(
        x=200, y=200, width=25, height=25, color=self.head_color, batch=self.sprite_batch)

        self.apple_sprite = pyglet.shapes.Rectangle(x=random.randint(200, self.width-250), y=random.randint(
        200, self.height-200), width=25, height=25, color=(255, 0, 0), batch=self.sprite_batch)
        self.sprite_list = [self.snake_sprite]

        # Schedule Update Function
        pyglet.clock.schedule_interval(self.update, 1 / 60)

    # Game Loop
    def on_draw(self): # Render
            self.clear()

            if self.alive:
                self.sprite_batch.draw()
                self.apple_sprite.draw()
                self.score_label.draw()
            else:
                self.death_label.draw()
                self.retry_label.draw()
 
    def on_key_press(self, symbol, modifiers): # Recieve Input
        if self.alive:
            if self.length > 1:
                if symbol == key.LEFT and self.direction != "R":
                    self.direction = "L"
                if symbol == key.RIGHT and self.direction != "L":
                    self.direction = "R"
                if symbol == key.UP and self.direction != "D":
                    self.direction = "U"
                if symbol == key.DOWN and self.direction != "U":
                    self.direction = "D"  
            else:
                if symbol == key.LEFT:
                    self.direction = "L"
                if symbol == key.RIGHT:
                    self.direction = "R"
                if symbol == key.UP:
                    self.direction = "U"
                if symbol == key.DOWN:
                    self.direction = "D"
        else:
            if symbol == key.SPACE:
                self.restart = True
    
    def update(self, dt): # Update
        self.move()
        self.follow()
        snake_apple_collision = h.Handles.collision(self.snake_sprite, self.apple_sprite)
        if snake_apple_collision:
            self.grow()
        self.body_collision()
        is_out_of_bounds = h.Handles.out_of_bounds(self.snake_sprite, self.width, self.height, self.kill)
    # Snake Functions 
    def move(self):
        # Delta time keeps movement consistent regardless of game slowdowns.
        if self.direction == "L":
            self.snake_sprite.x -= self.speed 
        elif self.direction == "R":
            self.snake_sprite.x += self.speed
        elif self.direction == "U":
            self.snake_sprite.y += self.speed
        elif self.direction == "D":
            self.snake_sprite.y -= self.speed
    
    def follow(self):
        pos = [[self.snake_sprite.x, self.snake_sprite.y]]
        list_length = len(self.sprite_list)
        for i in range(list_length):
            pos.append([self.sprite_list[i].x, self.sprite_list[i].y])

            last = pos[i - 1]
            current = pos[i]

            self.sprite_list[i].x = last[0]
            self.sprite_list[i].y = last[1]

            self.sprite_list[-1].visible = True

        return pos
    
    def grow(self):
        self.apple_sprite.x = random.randint(50, self.width-50)
        self.apple_sprite.y = random.randint(50, self.height-50)

        self.length += 1
        self.score_label.text = f"Score = {self.length - 1}"

        for i in range(8):
            self.sprite_list.append(pyglet.shapes.Rectangle(
                x=-100, y=-100, width=25, height=25, color=self.body_color, batch=self.sprite_batch))
        
        if self.length == 2:
            for i in self.sprite_list[:7]:
                i.color = self.head_color

    def body_collision(self):
        for i in self.sprite_list[7:]:
            if self.snake_sprite.position == i.position:
                self.alive = False
                self.kill()

    def kill(self):
        self.alive = False
        self.death_label.text =  f"You died! Your score was {self.length - 1}."
        pyglet.clock.unschedule(self.update)