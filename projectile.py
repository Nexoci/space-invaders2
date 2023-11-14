import pygame,sys

class Projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,image_to_use,speed=10):
        super().__init__()
        self.image = pygame.image.load(image_to_use)
        self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha() 
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = speed
    def move(self):
        self.rect.y -= self.speed
    def update(self):
        self.move()
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False
    def check_hit_group(self,group1,group2):
        if pygame.sprite.spritecollide(self,group1,group2, True, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False
class EProjectile(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,image_to_use,speed=6):
        super().__init__()
        self.image = pygame.image.load(image_to_use)
        self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha() 
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = speed
    def move(self):
        self.rect.y += self.speed
    def update(self):
        self.move()
    def death(self):
        self.rect.x = 9000
    def check_hit(self,group):
        if pygame.sprite.spritecollide(self,group, True, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False
        
    def check_hit_group(self,group1,group2):
        if pygame.sprite.groupcollide(self,group1,group2,True,True, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False
