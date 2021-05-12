import pyglet
from pyglet import shapes
import config as c

# Create Window
window = pyglet.window.Window(c.width, c.height, caption=c.caption)

# Create sprite batches
spriteBatch = pyglet.graphics.Batch()
sprite = shapes.Rectangle(x=200, y=200, width=25, height=25, color=(152, 255, 152), batch=spriteBatch)


@window.event
def on_draw():
    window.clear()
    spriteBatch.draw()


# Run
pyglet.app.run()