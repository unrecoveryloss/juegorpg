import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from interfaces.login import login_interface
from interfaces.register import register_interface

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego RPG - Inicio")

font = pygame.font.SysFont("Gothic", 36)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)

base_path = os.path.dirname(__file__)
bg_path = os.path.join(base_path, "..", "img", "bg.jpg")
bg_image = pygame.image.load(bg_path)
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

def draw_button(text, y, callback):
    rect = pygame.Rect(200, y, 200, 50)
    pygame.draw.rect(screen, GREEN, rect)
    text_surf = font.render(text, True, WHITE)
    screen.blit(text_surf, (rect.x + 20, rect.y + 10))
    return rect, callback

def main_menu():
    while True:
        screen.blit(bg_image, (0, 0))
        buttons = [
            draw_button("Iniciar sesión", 120, login_interface),
            draw_button("Registrarse", 200, register_interface),
        ]
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect, callback in buttons:
                    if rect.collidepoint(event.pos):
                        callback()

if __name__ == '__main__':
    main_menu()