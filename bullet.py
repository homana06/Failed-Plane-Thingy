import pygame
import math




class Bullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 10
        self.width = 5
        self.height = 10
        self.color = (255, 0, 0)

    def move(self, angle, x, y, surface):
        # Move the bullet in the direction defined by its angle
        while 0 <= x <= surface.get_width() and 0 <= y <= surface.get_height():
            x = x + self.speed * math.cos(math.radians(angle))
            y = y - self.speed * math.sin(math.radians(angle))  # Negative since y-coordinates increase downward
            self.draw(surface, x, y)
            pygame.display.update()  # Update the display to show the bullet's movement

    def draw(self, surface, x, y):
        pygame.draw.rect(surface, self.color, (x, y, self.width, self.height))

    def fire_from_sprite(self, surface, sprite_x, sprite_y, sprite_angle):
        # Calculate starting position based on sprite's position and rotation
        # Calculate the displacement of the bullets from the center of the sprite
        displacement_x = (self.height / 2) * math.sin(math.radians(sprite_angle))
        displacement_y = (self.height / 2) * math.cos(math.radians(sprite_angle))

        # Adjust the starting position to the top-center of the sprite
        start_x = sprite_x + displacement_x
        start_y = sprite_y - displacement_y - self.height  # Adjusted by subtracting the height of the bullet

        # Move the bullets from the adjusted starting position
        self.move(sprite_angle, start_x, start_y, surface)



#while True:
    #dy/dx - 4 
