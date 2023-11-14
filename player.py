import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_to_use,speed):
        super().__init__() 
        self.image = pygame.image.load(image_to_use)
        self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha() 
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.speed = speed
    def back(self):
        self.rect.x -= self.movex
    def move(self):
        key_input = pygame.key.get_pressed()
        self.movex = (key_input[pygame.K_LEFT] * -self.speed) + (key_input[pygame.K_RIGHT] * self.speed)
        self.rect.x += self.movex
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False
        
class Health(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image1,image2,image3,image4,h_amount=2):
        super().__init__() 
        self.image = pygame.image.load(image1)
        self.image2 = pygame.image.load(image2)
        self.image3 = pygame.image.load(image3)
        self.image4 = pygame.image.load(image4)
        self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha()
        self.image2 = pygame.transform.scale(self.image2 , (width, height)).convert_alpha()
        self.image3 = pygame.transform.scale(self.image3 , (width, height)).convert_alpha()
        self.image4 = pygame.transform.scale(self.image4 , (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = startX
        self.rect.y = startY
        self.health = h_amount
    def healthhit(self):
        self.health -= 1
        if self.health == 1:
            self.image = self.image2
        elif self.health == 0:
            self.image = self.image3
        else:
            self.image = self.image4
            
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False
