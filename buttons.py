import pygame
import sys

class with_background(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y,width,height, font_name,font_size,back_color,text_color,hover_color,back_hover_color,text,action):
        super().__init__()
        font_used = pygame.font.SysFont(font_name, font_size)
        self.image = pygame.Surface([width, height],pygame.SRCALPHA).convert_alpha()
        self.image.fill(back_color)
        out_text = font_used.render(text, True, text_color)
        self.text_width=out_text.get_width()
        self.text_height= out_text.get_height()
        
        self.image.blit(out_text, (((width-self.text_width)/2), ((height-self.text_height)/2)))
        self.rect = self.image.get_rect(topleft =(start_x,start_y))
        
        self.text_color = text_color
        self.hover_color=hover_color
        self.text=text
        self.action = action
        self.font_used = font_used
        self.back_color = back_color
        self.back_hover_color= back_hover_color
    def update(self,pos,event):               
        if self.rect.collidepoint(pos):          
            self.image.fill(self.back_hover_color)
            self.image.blit(self.font_used.render(self.text, True, self.hover_color), (((self.rect.width-self.text_width)/2), ((self.rect.height-self.text_height)/2)))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               self.action() 
        else:
            self.image.fill(self.back_color)
            self.image.blit(self.font_used.render(self.text, True, self.text_color), (((self.rect.width-self.text_width)/2), ((self.rect.height-self.text_height)/2)))

class no_background(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y, font_name,font_size,text_color,hover_color,text,action):
        super().__init__()
        font_used = pygame.font.SysFont(font_name, font_size)
        self.image =font_used.render(text, True, text_color)
        self.rect = self.image.get_rect(topleft =(start_x,start_y))
    
        self.text_color = text_color
        self.hover_color=hover_color
        self.text=text
        self.action = action
        self.font_used = font_used

    def update(self,pos,event):               
        if self.rect.collidepoint(pos):          
            self.image =self.font_used.render(self.text, True, self.hover_color)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               self.action() 
        else:
            self.image =self.font_used.render(self.text, True, self.text_color)
        
        
class imagebutton(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y,width, height, image_no, image_hover,action):
        super().__init__()        
        self.img_default = pygame.image.load(image_no) 
        self.img_hover = pygame.image.load(image_hover) 
        
        self.img_default = pygame.transform.scale(self.img_default , (width, height)).convert_alpha()
        self.img_hover = pygame.transform.scale(self.img_hover , (width, height)).convert_alpha()
        
        self.image = self.img_default
        self.mask  = pygame.mask.from_surface(self.image)
    
        self.rect = self.image.get_rect(topleft =(start_x,start_y))
        
        self.action = action

    def update(self,pos,event):               
        mouse_group=pygame.sprite.Group()
        mouse_group.add(Mouse_POS(pos)) 
        if pygame.sprite.spritecollide(self, mouse_group, False, collided=pygame.sprite.collide_mask):          
            self.image = self.img_hover
            self.mask  = pygame.mask.from_surface(self.image)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               self.action() 
        else:
            self.image =self.img_default
            self.mask  = pygame.mask.from_surface(self.image)
       
class Mouse_POS(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([1, 1])
        self.rect = self.image.get_rect(topleft =pos) 