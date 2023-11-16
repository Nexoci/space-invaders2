#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys,time
from player import Player
from player import Health
from projectile import Projectile
from projectile import EProjectile
from backround import backround
from buttons import imagebutton
from static import stillimage
from Enemy import Evil
from blockers import Blockers
import gifguy
import pygame,random
import sys

    

pygame.init()
def exit():
    pygame.quit()
    sys.exit()
def next():
    global done
    done=True

    
    
def gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT):
        spacer = 10
        font = pygame.font.SysFont('Consolas', 10)
        for gridX in range(0, WINDOW_WIDTH, spacer):        
            window.blit(pygame.transform.rotate(font.render(str(gridX), True, (255, 255, 255)),90),(gridX,0))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            window.blit(font.render(str(gridY), True, (255, 255, 255)), (0, gridY))
        for gridX in range(0, WINDOW_WIDTH, spacer):
            pygame.draw.line(window,(255,0,0),(gridX,0),(gridX,WINDOW_HEIGHT))
        for gridY in range(0, WINDOW_HEIGHT, spacer):
            pygame.draw.line(window,(255,0,0),(0,gridY),(WINDOW_WIDTH,gridY)) 
fps = 30
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
cooldown=fps/30
points = 0
Icon = pygame.image.load("images/spacers.jpg")
#Creating Groups
player_group = pygame.sprite.Group()
space_group = pygame.sprite.Group()
collision_group = pygame.sprite.Group()
start_group = pygame.sprite.Group()
starttext_group = pygame.sprite.Group()
start_btn= pygame.sprite.Group()
projectile_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
blocker_group = pygame.sprite.Group()
Health_group =pygame.sprite.Group()
Enemy_bullet =pygame.sprite.Group()
#creates window and custom objects
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
backgroundgif = gifguy.loadGIF('images/spacevader.gif')
back = gifguy.AnimatedSpriteObject(0,0,WINDOW_WIDTH, WINDOW_HEIGHT, backgroundgif)
backgroundstart = gifguy.loadGIF('images/startback.gif')
back2 = gifguy.AnimatedSpriteObject(0,0,WINDOW_WIDTH, WINDOW_HEIGHT, backgroundstart)

font = pygame.font.SysFont('Fixedsys', 30)
billy=Player(350,600,125,75,"images/billy.png",10)
for i in range(85,540,65):
    alien_group.add(Evil(i,200,125,100,"images/enemy1.png",5))
    alien_group.add(Evil(i,250,125,100,"images/enemy1.png",5))
    alien_group.add(Evil(i,300,125,100,"images/enemy1.png",5))

blocker1= Blockers(300,475,125,125,"blockers/good.png","blockers/hit.png","blockers/broken.png","blockers/damaged.png","blockers/destroyed.png",6)
blocker2= Blockers(560,475,125,125,"blockers/good.png","blockers/hit.png","blockers/broken.png","blockers/damaged.png","blockers/destroyed.png",6)
blocker3= Blockers(10,475,125,125,"blockers/good.png","blockers/hit.png","blockers/broken.png","blockers/damaged.png","blockers/destroyed.png",6)
Healthbars= Health(50,740,600,50,"images/healthbar.png","images/healthbar2.png","images/healthbar3.png","images/healthbarD.png")
help= stillimage(105,390,500,400,"images/help.png")
author= stillimage(275,75,150,100,"images/author.png")
btn_ply= imagebutton(225,100,250,250,"images/play.png","images/playclicked.png",next)
btn_ext= imagebutton(225,200,250,250,"images/exits.png","images/exitclicked.png",exit)
collidewalls=backround(WINDOW_WIDTH,WINDOW_HEIGHT,"images/collide.png")
title= stillimage(125,0,500,250,"images/title.png")
blocker_group.add(blocker1,blocker2,blocker3)
player_group.add(billy)
space_group.add(back)
Health_group.add(Healthbars)
start_btn.add(btn_ply,btn_ext)
start_group.add(back2,title,help,author)
collision_group.add(collidewalls)
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(Icon)
row = 0
def display():
    window.fill((255,255,255))
    collision_group.draw(window)
    space_group.draw(window)
    projectile_group.draw(window)
    alien_group.draw(window)
    player_group.draw(window)
    Health_group.draw(window)
    blocker_group.draw(window)
    Enemy_bullet.draw(window)
    window.blit(font.render(f"Points: {points}", True, (255, 255, 255)), (0, 0))
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
damage=3
done=False
while not done:
    window.fill((255,255,255))
    start_group.draw(window)
    start_btn.draw(window)
    #gridHelp(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        start_btn.update(pos,event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(fps)
    start_group.update(30)
E_bullet=None
while True:
    display()
    cooldown=cooldown-1
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if pygame.sprite.spritecollide(collidewalls, alien_group, False, pygame.sprite.collide_mask):
        row+=1
            
    for alien in alien_group:
        #alien.move()
        if alien.row != row:
            alien.rect.y += 15
            alien.row = row
            alien.direction = not alien.direction
        alien.move()
        num = random.randint(1,250)
        if alien.check_hit(projectile_group):
            points += 1000
            alien.kill()
            bullet.kill()
        if alien.check_hit(player_group):
            Healthbars.healthdead()
            billy.kill()
        if num == (1):
            E_bullet = EProjectile((alien.rect.x + 33), (alien.rect.centery - 40), 60, 32, "images/E_bullet.png")
            Enemy_bullet.add(E_bullet)
    for blockers in blocker_group:
        if blockers.check_hit(projectile_group):
            blockers.damage()
            bullet.kill()
        if blockers.check_hit(Enemy_bullet):
            pygame.sprite.spritecollide(blockers, Enemy_bullet, True, pygame.sprite.collide_mask)
            blockers.damage()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_SPACE] and cooldown<0:
        bullet = Projectile((billy.rect.x+33), (billy.rect.centery-40),60,32,"images/bullet.png")
        projectile_group.add(bullet) 
        cooldown=10
        if bullet.check_hit(alien_group):
            bullet.kill()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
    if billy.check_hit(collision_group):
        billy.back()
    hit_list = pygame.sprite.spritecollide(billy, Enemy_bullet, True, pygame.sprite.collide_mask)
    for E_bullet in hit_list:
        damage-=1
        Healthbars.healthhit()
        if damage == 0:
            billy.dead()
    #if billy.bullet_strike(Enemy_bullet):
        #damage-=1
        #Healthbars.healthhit()
        #E_bullet.kill()
        #if damage == 0:
            #billy.dead()
    #if billy.check_hit(Enemy_bullet):
        #E_bullet.kill()
        

            
        
    billy.move()
    space_group.update(30)
    projectile_group.update()  # Update the projectiles
    alien_group.update()
    blocker_group.update()
    Enemy_bullet.update()
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
