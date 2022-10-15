import random
import pygame
import sys

pygame.init()


class My:
    def __init__(self, screen):
        self.w = None
        self.h = None
        self.screen = screen
        self.mu_fish = pygame.image.load('./image/木鱼.png')
        self.my_rect = self.mu_fish.get_rect()
        self.my_rect.center = self.my_rect.topleft

    def display(self):
        self.w, self.h = pygame.display.get_surface().get_size()
        self.screen.blit(self.mu_fish, ((self.w - 311) / 2, (self.h - 263) / 2))


class Game:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.font_surface_2 = None
        self.mods = pygame.RESIZABLE
        self.screen = pygame.display.set_mode((800, 480), self.mods)
        self.ico = pygame.image.load("./ico/rope_crop.ico")
        pygame.display.set_icon(self.ico)
        pygame.display.set_caption('by Cloud sky', 'by Cloud sky')

        self.color_w = [(255, 159, 243), (95, 39, 205), (84, 160, 255), (0, 210, 211), (29, 209, 161), (72, 219, 251),
                        (255, 107, 107), (255, 107, 107), (254, 202, 87), (255, 159, 243)]
        self.color = random.choice(self.color_w)
        self.clock = pygame.time.Clock()

        # f = open("secret key/data.txt", "w")
        # f.write('0')
        # f.close()
        f = open("secret key/data.txt", "r")
        self.txt = int(f.readline(), 2)
        f.close()
        self.num = self.txt
        # self.num = 114513

        self.screen.fill(self.color)
        pygame.display.flip()

    def key(self, event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
                (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            if pygame.display.get_active():
                self.color = random.choice(self.color_w)
                if self.num == 114513:
                    pygame.mixer.music.load("./music/114514.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("./music/敲击木鱼.wav")
                    pygame.mixer.music.queue('./music/功德宝到账.mp3')
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play()
                self.x, self.y = pygame.mouse.get_pos()
                self.num += 1

        # if event.type == pygame.KEYDOWN and event.key == pygame.K_F11 and self.mods == pygame.RESIZABLE and \
        #         pygame.display.get_active():
        #     self.mods = pygame.FULLSCREEN
        #     self.screen = pygame.display.set_mode((800, 480), self.mods)

    def font(self):
        font = pygame.font.Font('./font/MiSans-Light.ttf', 40)
        font_surface = font.render('功德包余额：%d' % self.num, True, 'white')
        self.screen.blit(font_surface, (10, 1))
        font_2 = pygame.font.Font('./font/MiSans-Light.ttf', 20)
        self.font_surface_2 = font_2.render('功德+1', True, 'white')

    def display(self):
        my = My(self.screen)

        while True:
            self.screen.fill(self.color)

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    f = open("secret key/data.txt", "r")
                    txt = int(f.readline(), 2)
                    f.close()
                    if txt < self.num:
                        f = open("secret key/data.txt", "w")
                        f.write(str(bin(self.num)))
                        f.close()
                    pygame.quit()
                    sys.exit()

                self.key(event)
            my.display()
            self.font()
            self.screen.blit(self.font_surface_2, (self.x - 20, self.y - 25))

            pygame.display.update()

            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.display()