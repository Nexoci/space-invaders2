import pygame
import sys

class stillimage(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_to_use):
            super().__init__() 
            self.image = pygame.image.load(image_to_use)
            self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha() 
            self.mask  = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect(topleft=(startX,startY))
    def collide(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False