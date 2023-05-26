import pygame
import sys
from .elementGUI import element as el


class Visual:
    listaElPorti = []
    listaElHangar = []
    listaElPiste = []
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    def __init__(self):
        pygame.init()
        self.initElements()
        self.screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("Real Time Status Visualization")

    def initElements(self):
        self.listaElPiste.append(el(330, 411, 30, 30, self.GREEN))
        self.listaElPiste.append(el(530, 411, 30, 30, self.GREEN))
        self.listaElPorti.append(el(180, 120, 30, 30, self.GREEN))
        self.listaElPorti.append(el(350, 120, 30, 30, self.GREEN))
        self.listaElPorti.append(el(540, 120, 30, 30, self.GREEN))
        self.listaElPorti.append(el(700, 120, 30, 30, self.GREEN))
        self.listaElHangar.append(el(770, 220, 30, 30, self.GREEN))

    def init_layout(self):
        imagine = pygame.image.load(
            r"D:\NASA\ProiectAvionV2\src\GUI\img\strada.jpg")
        imagineGate = pygame.image.load(
            r"D:\NASA\ProiectAvionV2\src\GUI\img\gate.jpg")
        imagineHangar = pygame.image.load(
            r"D:\NASA\ProiectAvionV2\src\GUI\img\hangar.png")
        imagineGate = pygame.transform.scale(imagineGate, (90, 90))
        imagine = pygame.transform.scale(imagine, (70, 139))
        imagineHangar = pygame.transform.scale(imagineHangar, (90, 90))
        self.screen.blit(imagine, (250, 411))
        self.screen.blit(imagine, (450, 411))
        self.screen.blit(imagineGate, (90, 120))
        self.screen.blit(imagineGate, (260, 120))
        self.screen.blit(imagineGate, (450, 120))
        self.screen.blit(imagineGate, (610, 120))
        self.screen.blit(imagineHangar, (790, 220))

    def run(self):
        self.screen.fill((30, 70, 120))
        self.init_layout()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for element1 in self.listaElPiste:
                pygame.draw.rect(self.screen, element1.culoare, (element1.pozitie_inaltime,
                                                                 element1.pozitie_latime, element1.latime, element1.lungime))
            for element1 in self.listaElPorti:
                pygame.draw.rect(self.screen, element1.culoare, (element1.pozitie_inaltime,
                                                                 element1.pozitie_latime, element1.latime, element1.lungime))
            for element1 in self.listaElHangar:
                pygame.draw.rect(self.screen, element1.culoare, (element1.pozitie_inaltime,
                                                                 element1.pozitie_latime, element1.latime, element1.lungime))
            pygame.display.flip()
