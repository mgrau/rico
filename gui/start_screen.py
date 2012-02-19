import pygame
import tiles
import fonts
import sys

try:
    import android
except ImportError:
    android = None


class Button():
    def __init__(self):
        self.surface = pygame.Surface((40,40))
        self.rect = pygame.Rect(0,0,40,40)

class Start_Screen():
    def __init__(self,screen):
        self.screen = screen
        self.players = []

        self.player_list = pygame.Surface((40,40))

        self.add_player = Button()
        self.add_player.surface = fonts.h1.render("Add Player",1,(255,255,255),(100,0,0))
        self.add_player.rect = self.add_player.surface.get_rect()
        self.add_player.rect.topleft = (500,25)

        self.del_player = Button()
        self.del_player.surface = fonts.h2.render("Remove Player",1,(255,255,255),(100,0,0))
        self.del_player.rect = self.del_player.surface.get_rect()
        self.del_player.rect.topleft = (500,100)

        self.ai_on = Button()
        self.ai_on.surface = fonts.h2.render("AI",1,(64,64,255),(192,192,192))
        self.ai_on.rect = self.ai_on.surface.get_rect()
        self.ai_on.rect.topleft = (500,150)

        self.ai_off = Button()
        self.ai_off.surface = fonts.h2.render("AI",1,(128,128,128),(192,192,192))
        self.ai_off.rect = self.ai_off.surface.get_rect()
        self.ai_off.rect.topleft = (500,150)

        self.invert_on = Button()
        self.invert_on.surface = fonts.h2.render("Invert",1,(64,64,255),(192,192,192))
        self.invert_on.rect = self.invert_on.surface.get_rect()
        self.invert_on.rect.topleft = (550,150)

        self.invert_off = Button()
        self.invert_off.surface = fonts.h2.render("Invert",1,(128,128,128),(192,192,192))
        self.invert_off.rect = self.invert_off.surface.get_rect()
        self.invert_off.rect.topleft = (550,150)

        self.done = Button()
        self.done.surface = fonts.h1.render("Done",1,(255,255,255),(100,0,0))
        self.done.rect = self.done.surface.get_rect()
        self.done.rect.topleft = (500,200)

        self.name = Button()
        self.name.surface = fonts.h1.render("",1,(0,0,0),(255,255,255))
        self.name.rect = self.name.surface.get_rect()
        self.name.rect.topleft = (25,25)

        self.name_box = pygame.Rect((25,25,400,self.name.rect.height))

    def draw(self):
        self.screen.blit(tiles.island,(0,0))
        self.screen.blit(self.add_player.surface,self.add_player.rect)
        self.screen.blit(self.del_player.surface,self.del_player.rect)
        self.screen.blit(self.done.surface,self.done.rect)
        self.screen.blit(self.ai_off.surface,self.ai_off.rect)
        self.screen.blit(self.invert_off.surface,self.invert_off.rect)
        pygame.draw.rect(self.screen,(255,255,255),self.name_box)
        self.screen.blit(self.name.surface,self.name.rect)
        pygame.display.update()

    def get_player(self):
        name = ""
        ai = False
        invert = False
        shift = False
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    shift = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_RETURN:
                        self.add_player_to_list(name,ai,invert)
                        name = ""
                        pygame.display.update(self.name_box)
                    elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        shift = True
                    elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                        self.name.surface = fonts.h1.render(name,1,(0,0,0),(255,255,255))
                        pygame.draw.rect(self.screen,(255,255,255),self.name_box)
                        self.screen.blit(self.name.surface,self.name.rect)
                        pygame.display.update(self.name_box)
                    elif event.key in [32]+range(48,58)+range(97,123):
                        if shift and event.key in range(97,123):
                            name += chr(event.key).capitalize()
                        else:
                            name += chr(event.key)
                        self.name.surface = fonts.h1.render(name,1,(0,0,0),(255,255,255))
                        self.screen.blit(self.name.surface,self.name.rect)
                        pygame.display.update(self.name_box)
                    else:
                        print event.key
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.add_player.rect.collidepoint(event.pos):
                        self.add_player_to_list(name,ai,invert)
                        name = ""
                    elif self.del_player.rect.collidepoint(event.pos):
                        if len(self.players):
                            self.players.pop()
                            self.draw_player_list()
                    elif self.done.rect.collidepoint(event.pos):
                        if android:
                            android.hide_keyboard()
                        return self.players
                    elif self.ai_off.rect.collidepoint(event.pos):
                        ai = not ai
                        if ai:
                            self.screen.blit(self.ai_on.surface,self.ai_on.rect)
                        else:
                            self.screen.blit(self.ai_off.surface,self.ai_off.rect)
                        pygame.display.update(self.ai_off.rect)
                    elif self.invert_off.rect.collidepoint(event.pos):
                        invert = not invert
                        if invert:
                            self.screen.blit(self.invert_on.surface,self.invert_on.rect)
                        else:
                            self.screen.blit(self.invert_off.surface,self.invert_off.rect)
                        pygame.display.update(self.invert_off.rect)
                    elif self.name_box.collidepoint(event.pos):
                        if android:
                            android.show_keyboard()
                    else:
                        if android:
                            android.hide_keyboard()


    def add_player_to_list(self,name,ai=False,invert=False):
        if name:
            self.players.append((name,ai,invert))
            self.name.surface = fonts.h1.render("",1,(0,0,0),(255,255,255))
            pygame.draw.rect(self.screen,(255,255,255),self.name_box)
            self.screen.blit(self.name.surface,self.name.rect)
            pygame.display.update(self.name_box)
            self.draw_player_list()

    def draw_player_list(self):
        self.screen.blit(tiles.island,(50,100,300,500),(50,100,300,500))
        for i,player in enumerate(self.players):
            if player[1]:
                self.screen.blit(fonts.h2.render(str(i+1)+") "+player[0]+" (AI)",1,(255,255,255)),(50,100+25*i))
            else:
                self.screen.blit(fonts.h2.render(str(i+1)+") "+player[0],1,(255,255,255)),(50,100+25*i))
        pygame.display.update((50,100,300,500))