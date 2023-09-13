import random
from time import sleep

import pygame
from pygame.locals import *

# Game Setting
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (250, 250, 50)
RED = (250, 50, 50)

FPS = 60


# Fighter == Game User Class(Sprite Class)
class Fighter(pygame.sprite.Sprite):
    # Element initialization
    def __init__(self):
        super(Fighter, self).__init__()
        self.image = pygame.image.load('img/fighter/fighter.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(WINDOW_WIDTH / 2)
        self.rect.y = WINDOW_HEIGHT - self.rect.height
        self.dx = 0
        self.dy = 0

    # Sprite moving localization += Game Screen
    # Don't escape Game Screen
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.x < 0 or self.rect.x + self.rect.width > WINDOW_WIDTH:
            self.rect.x -= self.dx

        if self.rect.y < 0 or self.rect.y + self.rect.height > WINDOW_HEIGHT:
            self.rect.y -= self.dy

    # Draw Sprite Object in the Game Screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # If the Fighter collide the enemies, the fighter explores in the game screen
    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite


# Missile Class => Fighter shoots the enemy
class Missile(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Missile, self).__init__()
        self.image = pygame.image.load('img/missile/missile.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound('music/missile/missile.wav')

    # the missile sound
    def launch(self):
        self.sound.play()

    # shoot the missile
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y + self.rect.height < 0:
            self.kill()

    # hit the aim
    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite


# The Rock Class ==> The enemies
class Rock(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Rock, self).__init__()
        rock_images = ('img/rock/rock01.png', 'img/rock/rock02.png', 'img/rock/rock03.png', 'img/rock/rock04.png', 'img/rock/rock05.png', \
                       'img/rock/rock06.png', 'img/rock/rock07.png', 'img/rock/rock08.png', 'img/rock/rock09.png', 'img/rock/rock10.png', \
                       'img/rock/rock11.png', 'img/rock/rock12.png', 'img/rock/rock13.png', 'img/rock/rock14.png', 'img/rock/rock15.png', \
                       'img/rock/rock16.png', 'img/rock/rock17.png', 'img/rock/rock18.png', 'img/rock/rock19.png', 'img/rock/rock20.png', \
                       'img/rock/rock21.png', 'img/rock/rock22.png', 'img/rock/rock23.png', 'img/rock/rock24.png', 'img/rock/rock25.png', \
                       'img/rock/rock26.png', 'img/rock/rock27.png', 'img/rock/rock28.png', 'img/rock/rock29.png', 'img/rock/rock30.png')
        self.image = pygame.image.load(random.choice(rock_images))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed

    # rock flow down the game screen
    def update(self):
        self.rect.y += self.speed

    # keeps going down the game screen
    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT:
            return True


# draw game
def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)


# If the fighter and rock meet each other, the explosion occurs
def occur_explosion(surface, x, y):
    explosion_image = pygame.image.load('img/explosion/explosion.png')
    explosion_rect = explosion_image.get_rect()
    explosion_rect.x = x
    explosion_rect.y = y
    surface.blit(explosion_image, explosion_rect)

    explosion_sounds = ('music/explosion/explosion01.wav', 'music/explosion/explosion02.wav', 'music/explosion/explosion03.wav')
    explosion_sound = pygame.mixer.Sound(random.choice(explosion_sounds))
    explosion_sound.play()


# Looping the game
def game_loop():
    default_font = pygame.font.Font('NanumGothic.ttf', 28)
    background_image = pygame.image.load('img/background/background.png')
    gameover_sound = pygame.mixer.Sound('music/gameover/gameover.wav')
    pygame.mixer.music.load('music/music/music.wav')
    pygame.mixer.music.play(-1)
    fps_clock = pygame.time.Clock()

    fighter = Fighter()
    missiles = pygame.sprite.Group()
    rocks = pygame.sprite.Group()

    occur_prob = 40
    shot_count = 0
    count_missed = 0

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    fighter.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    fighter.dx += 5
                elif event.key == pygame.K_UP:
                    fighter.dy -= 5
                elif event.key == pygame.K_DOWN:
                    fighter.dy += 5
                elif event.key == pygame.K_SPACE:
                    missile = Missile(fighter.rect.centerx, fighter.rect.y, 10)
                    missile.launch()
                    missiles.add(missile)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter.dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    fighter.dy = 0

        screen.blit(background_image, background_image.get_rect())

        occur_of_rocks = 1 + int(shot_count / 300)
        min_rock_speed = 1 + int(shot_count / 200)
        max_rock_speed = 1 + int(shot_count / 100)

        if random.randint(1, occur_prob) == 1:
            for i in range(occur_of_rocks):
                speed = random.randint(min_rock_speed, max_rock_speed)
                rock = Rock(random.randint(0, WINDOW_WIDTH - 30), 0, speed)
                rocks.add(rock)

        draw_text('파괴한 운석: {}'.format(shot_count), default_font, screen, 100, 20, YELLOW)
        draw_text('놓친 운석: {}'.format(count_missed), default_font, screen, 400, 20, RED)

        for missile in missiles:
            rock = missile.collide(rocks)
            if rock:
                missile.kill()
                rock.kill()
                occur_explosion(screen, rock.rect.x, rock.rect.y)
                shot_count += 1

        for rock in rocks:
            if rock.out_of_screen():
                rock.kill()
                count_missed += 1

        rocks.update()
        rocks.draw(screen)
        missiles.update()
        missiles.draw(screen)
        fighter.update()
        fighter.draw(screen)
        pygame.display.flip()

        if fighter.collide(rocks) or count_missed >= 3:
            pygame.mixer_music.stop()
            occur_explosion(screen, fighter.rect.x, fighter.rect.y)
            pygame.display.update()
            gameover_sound.play()
            sleep(1)
            done = True

        fps_clock.tick(FPS)

    return 'game_menu'


def game_menu():
    start_image = pygame.image.load('img/background/background.png')
    screen.blit(start_image, [0, 0])
    draw_x = int(WINDOW_WIDTH / 2)
    draw_y = int(WINDOW_HEIGHT / 4)
    font_70 = pygame.font.Font('NanumGothic.ttf', 70)
    font_40 = pygame.font.Font('NanumGothic.ttf', 40)

    draw_text('지구를 지켜라!', font_70, screen, draw_x, draw_y, YELLOW)
    draw_text('엔터 키를 누르면', font_40, screen, draw_x, draw_y + 200, WHITE)
    draw_text('게임이 시작됩니다.', font_40, screen, draw_x, draw_y + 250, WHITE)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 'play'
        if event.type == QUIT:
            return 'quit'

    return 'game_menu'


def main():
    global screen

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('PyShooting')

    action = 'game_menu'
    while action != 'quit':
        if action == 'game_menu':
            action = game_menu()
        elif action == 'play':
            action = game_loop()

    pygame.quit()


if __name__ == "__main__":
    main()