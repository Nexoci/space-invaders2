import pygame
from PIL import Image, ImageSequence


def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygameImage)
    return frames
 
class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image =  pygame.transform.scale(self.images[0], (width, height))
     
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image_index = 0
        self.timer=0
    def update(self,speed):
        self.timer+=10
        if self.timer >=speed:
            self.image_index += 1
           # self.image = self.images[self.image_index % len(self.images)]
            self.image =  pygame.transform.scale(self.images[self.image_index % len(self.images)], (self.rect.width, self.rect.height))
            self.timer=0


