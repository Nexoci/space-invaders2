import pygame,sys


class Blockers(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y,width,height,image1,image2,image3,image4,image5,hits):
        super().__init__() 
        self.image = pygame.image.load(image1)
        self.image2 = pygame.image.load(image2)
        self.image3 = pygame.image.load(image3)
        self.image4 = pygame.image.load(image4)
        self.image5 = pygame.image.load(image5)
        self.image5 = pygame.transform.scale(self.image5 , (width, height)).convert_alpha()
        self.image4 = pygame.transform.scale(self.image4 , (width, height)).convert_alpha()
        self.image3 = pygame.transform.scale(self.image3 , (width, height)).convert_alpha()
        self.image = pygame.transform.scale(self.image , (width, height)).convert_alpha()
        self.image2 = pygame.transform.scale(self.image2 , (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.health=hits
    def damage(self):
        self.health -= 1
        if self.health == 3:
            self.image = self.image2
        elif self.health == 2:
            self.image = self.image3
        elif self.health == 1:
            self.image = self.image4
        elif self.health == 0:
            self.image = self.image5
        else:
            self.kill()
            self.rect.x = 9000
    def check_hit(self,group1):
        if pygame.sprite.spritecollide(self,group1, False, collided=pygame.sprite.collide_mask):
            return True
        else:
            return False