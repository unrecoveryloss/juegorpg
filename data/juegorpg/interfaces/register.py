import pygame
import sys
import requests

pygame.init()
WIDTH, HEIGHT = 600, 400
font = pygame.font.SysFont(None, 28)
small_font = pygame.font.SysFont(None, 20)

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
DARK_GRAY = (80, 80, 80)
GREEN = (34, 139, 34)
RED = (200, 30, 30)
LIGHT_GREEN = (30, 200, 100)
ACTIVE = (120, 120, 120)

def draw_button(screen, text, rect, color=GREEN):
    pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def register_interface():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Registro de Usuario")

    usuario = ""
    correo = ""
    contraseña = ""
    active_field = "usuario"
    mensaje = ""
    mensaje_color = RED

    input_x = 230
    input_width = 280
    input_height = 32

    usuario_rect = pygame.Rect(input_x, 100, input_width, input_height)
    correo_rect = pygame.Rect(input_x, 150, input_width, input_height)
    contraseña_rect = pygame.Rect(input_x, 200, input_width, input_height)

    registrar_btn = pygame.Rect(100, 320, 180, 40)
    volver_btn = pygame.Rect(320, 320, 180, 40)

    while True:
        screen.fill(GRAY)

        title = font.render("Registro de Usuario", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

        pygame.draw.rect(screen, ACTIVE if active_field == "usuario" else DARK_GRAY, usuario_rect)
        pygame.draw.rect(screen, ACTIVE if active_field == "correo" else DARK_GRAY, correo_rect)
        pygame.draw.rect(screen, ACTIVE if active_field == "contraseña" else DARK_GRAY, contraseña_rect)

        screen.blit(font.render("Usuario:", True, WHITE), (100, 105))
        screen.blit(font.render(usuario, True, WHITE), (usuario_rect.x + 5, usuario_rect.y + 5))

        screen.blit(font.render("Correo:", True, WHITE), (100, 155))
        screen.blit(font.render(correo, True, WHITE), (correo_rect.x + 5, correo_rect.y + 5))

        screen.blit(font.render("Contraseña:", True, WHITE), (100, 205))
        screen.blit(font.render("*" * len(contraseña), True, WHITE), (contraseña_rect.x + 5, contraseña_rect.y + 5))

        requisitos = small_font.render("Usuario ≥ 4 letras | Correo válido | Contraseña ≥ 6 caracteres", True, WHITE)
        screen.blit(requisitos, (100, 245))

        mensaje_text = font.render(mensaje, True, mensaje_color)
        screen.blit(mensaje_text, (100, 270))

        draw_button(screen, "Registrarse", registrar_btn)
        draw_button(screen, "Volver al menú", volver_btn)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if usuario_rect.collidepoint(event.pos):
                    active_field = "usuario"
                elif correo_rect.collidepoint(event.pos):
                    active_field = "correo"
                elif contraseña_rect.collidepoint(event.pos):
                    active_field = "contraseña"
                elif registrar_btn.collidepoint(event.pos):
                    if not usuario.strip() or not correo.strip() or not contraseña.strip():
                        mensaje = "Completa todos los campos"
                        mensaje_color = RED
                    elif len(usuario.strip()) < 4:
                        mensaje = "Usuario demasiado corto"
                        mensaje_color = RED
                    elif "@" not in correo.strip() or "." not in correo.strip():
                        mensaje = "Correo inválido"
                        mensaje_color = RED
                    elif len(contraseña.strip()) < 6:
                        mensaje = "Contraseña muy débil"
                        mensaje_color = RED
                    else:
                        try:
                            response = requests.post("http://127.0.0.1:5000/auth/register", json={
                                "usuario": usuario.strip(),
                                "correo": correo.strip(),
                                "contraseña": contraseña.strip()
                            })
                            data = response.json()
                            if data.get("success"):
                                mensaje = data.get("message", "Registro exitoso")
                                mensaje_color = LIGHT_GREEN
                            else:
                                mensaje = data.get("message", "Error en el registro")
                                mensaje_color = RED
                        except Exception as e:
                            mensaje = f"Error: {str(e)}"
                            mensaje_color = RED

                elif volver_btn.collidepoint(event.pos):
                    from interfaces.home import main_menu
                    main_menu()
                    return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    if active_field == "usuario":
                        active_field = "correo"
                    elif active_field == "correo":
                        active_field = "contraseña"
                    else:
                        active_field = "usuario"
                elif event.key == pygame.K_BACKSPACE:
                    if active_field == "usuario":
                        usuario = usuario[:-1]
                    elif active_field == "correo":
                        correo = correo[:-1]
                    else:
                        contraseña = contraseña[:-1]
                else:
                    if active_field == "usuario" and len(usuario) < 20:
                        usuario += event.unicode
                    elif active_field == "correo" and len(correo) < 40:
                        correo += event.unicode
                    elif active_field == "contraseña" and len(contraseña) < 20:
                        contraseña += event.unicode
