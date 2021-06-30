class Handles:
    """
    A static class of functions that handle events during gameplay.
    """
    @staticmethod
    def collision(sprite, target):
        if target.x < sprite.x + target.width and \
            target.x + target.width > sprite.x and \
            target.y < sprite.y + sprite.height and \
            target.y + target.height > sprite.y:
            return True
        else:
            return False
    
    @staticmethod
    def out_of_bounds(sprite, width, height, func):
        if sprite.x > width or sprite.x < 0:
            func()
        elif sprite.y > height or sprite.y < 0:
            func()

