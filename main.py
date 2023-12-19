import pygame
import os
import random

pygame.font.init()

width, height = 1024, 750

protagonista = pygame.image.load(os.path.join("assets", "Ship_combat.png"))

enemigo = pygame.image.load(os.path.join("assets", "Ship_enemy.png"))

bala = pygame.image.load(os.path.join("assets", "Bulle.png"))

fondo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Fondo.png")), (width, height))

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

class Bala:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    
    def move(self, vel):
        self.y += vel
    
    def off_screen(self, h):
        return not(self.y <= h and self.y >= 0)
    
    def collision(self, obj):
        return collide(obj)

class Ship:

    cooldown = 100

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.bullet_img = None
        self.bullets = []
        self.cool_down_conter = 0
    
    def draw(self, pantalla):
        pantalla.blit(self.ship_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(pantalla)
    
    def enfriamiento(self):
        if self.cool_down_conter >= self.cooldown:
            self.cool_down_conter = 0
        elif self.cool_down_conter > 0:
            self.cool_down_conter += 1

    def move_bullets(self, vel, obj):
        self.enfriamiento()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(height):
                self.bullets.remove(bullet)
            elif bullet.collision(obj):
                obj.health -= 10
                self.lasers.remove(bullet)


window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Proyecto tirador")


def main_menu():
    title_font = pygame.font.SysFont("helvetica", 70)
    run = True

    while run:
        window.blit(fondo, (0, 0))
        title_label = title_font.render("Presiona el mouse para iniciar...", 3, (36,85,216))
        title_pos = (width/2 - title_label.get_width()/2, 350)
        window.blit(title_label, title_pos)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

main_menu()
