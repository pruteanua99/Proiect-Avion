import pygame
import sys
from .elementGUI import element as el


class Visual:
    listaElPorti = []
    listaElHangar = []
    listaElPiste = []
    listaElButon = []
    lista_ref_NO = [None, None, None, None, None]
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    def __init__(self):
        self.initElements()
        pass

    def update_refNO(self):
        text_color = (255, 120, 0)
        font = pygame.font.Font(None, 32)
        for index, refno in enumerate(self.lista_ref_NO):
            text = font.render(refno, True, text_color)
            if index == 0 and refno == None:
                color = (30, 70, 120)
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect((90, 210), (100, 40)))
            elif index == 1 and refno == None:
                color = (30, 70, 120)
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect((260, 210), (100, 40)))
            elif index == 2 and refno == None:
                color = (30, 70, 120)
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect((450, 210), (100, 40)))
            elif index == 3 and refno == None:
                color = (30, 70, 120)
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect((610, 210), (100, 40)))
            elif index == 4 and refno == None:
                color = (30, 70, 120)
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect((770, 300), (100, 40)))
            elif index == 0:
                self.screen.blit(text, (100, 220))
            elif index == 1:
                self.screen.blit(text, (270, 220))
            elif index == 2:
                self.screen.blit(text, (460, 220))
            elif index == 3:
                self.screen.blit(text, (620, 220))
            elif index == 4:
                self.screen.blit(text, (780, 310))

    def initElements(self):
        self.listaElPiste.append(el(330, 411, 30, 30, self.GREEN))
        self.listaElPiste.append(el(530, 411, 30, 30, self.GREEN))
        self.listaElPorti.append(el(180, 120, 30, 30, self.GREEN))
        self.listaElPorti.append(el(350, 120, 30, 30, self.GREEN))
        self.listaElPorti.append(el(540, 120, 30, 30, self.GREEN))
        self.listaElPorti.append(el(700, 120, 30, 30, self.GREEN))
        self.listaElHangar.append(el(770, 220, 30, 30, self.GREEN))
        self.listaElButon.append(el(150, 411, 10, 10, self.GREEN))
        self.listaElButon.append(el(150, 500, 10, 10, self.GREEN))

    def init_text(self):
        text_color = (255, 120, 0)
        font = pygame.font.Font(None, 30)
        text = font.render("DOM - 1", True, text_color)
        self.screen.blit(text, (100, 95))
        text = font.render("DOM - 2", True, text_color)
        self.screen.blit(text, (270, 95))
        text = font.render("DOM - 3", True, text_color)
        self.screen.blit(text, (460, 95))
        text = font.render("INT - 1", True, text_color)
        self.screen.blit(text, (620, 95))
        text = font.render("HAN - 1", True, text_color)
        self.screen.blit(text, (800, 195))
        text = font.render("R1", True, text_color)
        self.screen.blit(text, (270, 560))
        text = font.render("R2", True, text_color)
        self.screen.blit(text, (470, 560))

    def init_layout(self):
        imagine = pygame.image.load(
            r"D:\NASA\ProiectAvionV2\src\GUI\img\strada.jpg")
        imagineGate = pygame.image.load(
            r"D:\NASA\ProiectAvionV2\src\GUI\img\gate.jpg")
        imagineHangar = pygame.image.load(
            r"D:\NASA\ProiectAvionV2\src\GUI\img\hangar.png")
        imagineLanding = pygame.image.load(
            r"D:\NASA\ProiectAvionV2\src\GUI\img\landing.jpg")
        imagineDeparture = pygame.image.load(
            r"D:\NASA\ProiectAvionV2\src\GUI\img\departure.jpg")
        imagineSchema = pygame.image.load(
            r"D:\NASA\ProiectAvionV2\src\GUI\img\airport4.png")
        imagineLanding = pygame.transform.scale(imagineLanding, (40, 40))
        imagineDeparture = pygame.transform.scale(imagineDeparture, (40, 40))
        imagineSchema = pygame.transform.scale(imagineSchema, (400, 250))
        imagineGate = pygame.transform.scale(imagineGate, (90, 90))
        imagine = pygame.transform.scale(imagine, (70, 139))
        imagineHangar = pygame.transform.scale(imagineHangar, (90, 90))
        self.screen.blit(imagineSchema, (250, 200))
        self.screen.blit(imagineLanding, (100, 411))
        self.screen.blit(imagineDeparture, (100, 500))
        self.screen.blit(imagine, (250, 411))
        self.screen.blit(imagine, (450, 411))
        self.screen.blit(imagineGate, (90, 120))
        self.screen.blit(imagineGate, (260, 120))
        self.screen.blit(imagineGate, (450, 120))
        self.screen.blit(imagineGate, (610, 120))
        self.screen.blit(imagineHangar, (790, 220))

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("Real Time Status Visualization")
        self.screen.fill((30, 70, 120))
        self.init_layout()
        self.init_text()
        while True:
            self.update_refNO()
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
            for element1 in self.listaElButon:
                pygame.draw.rect(self.screen, element1.culoare, (element1.pozitie_inaltime,
                                                                 element1.pozitie_latime, element1.latime, element1.lungime))
            pygame.display.flip()
