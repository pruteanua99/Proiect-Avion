import pygame
import threading
import time


def pygame_thread():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fereastră Pygame")

    color = (0, 255, 0)  # Culoarea inițială a patratului

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Logica Pygame
        screen.fill((255, 255, 255))
        # Desenare patrat cu culoarea curentă
        pygame.draw.rect(screen, color, (100, 100, 200, 200))
        pygame.display.update()

    pygame.quit()


def main_thread():
    # Restul codului tău
    while True:
        # Logica programului principal
        print("Programul rulează în mod normal")


if __name__ == "__main__":
    pygame_thread = threading.Thread(target=pygame_thread)
    pygame_thread.start()

    main_thread()
