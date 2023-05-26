import threading
import pygame
from pygame.locals import *

# Variabila globală pentru starea culorii
color = (0, 255, 0)  # Verde

# Funcție pentru firul de execuție al interacțiunii cu consola


def console_thread():
    global color

    while True:
        user_input = input("Introduceți o opțiune (r - roșu, g - verde): ")

        if user_input == 'r':
            color = (255, 0, 0)  # Roșu
        elif user_input == 'g':
            color = (0, 255, 0)  # Verde

# Funcție pentru firul de execuție principal al ferestrei Pygame


def pygame_thread1():
    # Inițializarea Pygame
    pygame.init()

    # Dimensiunile ferestrei
    width = 400
    height = 400

    # Crearea ferestrei
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Schimbarea culorilor")

    # Bucla principală de evenimente
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Umplerea ferestrei cu culoarea de fundal
        window.fill((255, 255, 255))

        # Desenarea patratului cu culoarea corespunzătoare
        pygame.draw.rect(window, color, (100, 100, 200, 200))

        # Actualizarea ecranului
        pygame.display.flip()

    # Închiderea Pygame
    pygame.quit()


# Crearea și pornirea firelor de execuție
console_thread = threading.Thread(target=console_thread)
pygame_thread = threading.Thread(target=pygame_thread1)

console_thread.start()
pygame_thread.start()

# Așteptarea terminării firelor de execuție
console_thread.join()
pygame_thread.join()
