import pygame
import sys
import requests

pygame.init()
WIDTH, HEIGHT = 600, 400
font = pygame.font.SysFont(None, 28)

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
DARK_GRAY = (80, 80, 80)
GREEN = (34, 139, 34)
RED = (200, 30, 30)
ACTIVE = (120, 120, 120)

def draw_button(screen, text, rect, color=GREEN):
    pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def login_interface():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Iniciar Sesión")

    usuario = ""
    contraseña = ""
    active_field = "usuario"
    mensaje = ""

    input_x = 230
    input_width = 280
    input_height = 32

    usuario_rect = pygame.Rect(input_x, 120, input_width, input_height)
    contraseña_rect = pygame.Rect(input_x, 170, input_width, input_height)

    login_btn = pygame.Rect(100, 280, 180, 40)
    volver_btn = pygame.Rect(320, 280, 180, 40)

    while True:
        screen.fill(GRAY)

        title = font.render("Inicio de Sesión", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

        pygame.draw.rect(screen, ACTIVE if active_field == "usuario" else DARK_GRAY, usuario_rect)
        pygame.draw.rect(screen, ACTIVE if active_field == "contraseña" else DARK_GRAY, contraseña_rect)

        screen.blit(font.render("Usuario:", True, WHITE), (100, 127))
        screen.blit(font.render(usuario, True, WHITE), (usuario_rect.x + 5, usuario_rect.y + 5))

        screen.blit(font.render("Contraseña:", True, WHITE), (100, 177))
        screen.blit(font.render("*" * len(contraseña), True, WHITE), (contraseña_rect.x + 5, contraseña_rect.y + 5))

        mensaje_text = font.render(mensaje, True, RED)
        screen.blit(mensaje_text, (100, 230))

        draw_button(screen, "Iniciar sesión", login_btn)
        draw_button(screen, "Volver al menú", volver_btn)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if usuario_rect.collidepoint(event.pos):
                    active_field = "usuario"
                elif contraseña_rect.collidepoint(event.pos):
                    active_field = "contraseña"
                elif login_btn.collidepoint(event.pos):
                    if not usuario.strip() or not contraseña.strip():
                        mensaje = "Completa todos los campos"
                    else:
                        try:
                            response = requests.post("http://127.0.0.1:5000/auth/login", json={
                                "usuario": usuario.strip(),
                                "contraseña": contraseña.strip()
                            })
                            data = response.json()
                            if response.status_code == 200 and data.get("success"):
                                mensaje = f"¡Bienvenido {data['user']['nombre_usuario']} (Rol: {data['user']['id_rol']})!"
                            else:
                                mensaje = data.get("message", "Credenciales inválidas")
                        except Exception as e:
                            mensaje = f"Error: {str(e)}"

                elif volver_btn.collidepoint(event.pos):
                    from interfaces.home import main_menu
                    main_menu()
                    return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    active_field = "contraseña" if active_field == "usuario" else "usuario"
                elif event.key == pygame.K_BACKSPACE:
                    if active_field == "usuario":
                        usuario = usuario[:-1]
                    else:
                        contraseña = contraseña[:-1]
                else:
                    if active_field == "usuario" and len(usuario) < 20:
                        usuario += event.unicode
                    elif active_field == "contraseña" and len(contraseña) < 20:
                        contraseña += event.unicode
