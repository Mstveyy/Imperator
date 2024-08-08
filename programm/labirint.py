# Разработай свою игру в этом файле!
from pygame import*
from time import sleep
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed 

    def update(self):
        if zombi.rect.x <= width-80 and zombi.x_speed > 0 or zombi.rect.x >= 0 and zombi.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if zombi.rect.y <= height-80 and zombi.y_speed > 0 or zombi.rect.y >= 0 and zombi.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)

                
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        if self.rect.x <= 450:
            self.side = "right"
        if self.rect.x >= width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
                        




 

                 
width = 700
height = 500
zombi = Player('zombi-removebg-preview.png', 5, height -  80,80,80,0,0)
circle = Enemy('balll.png', width - 80, 150, 80, 80, 5)
barriers = sprite.Group()
wall_1 = GameSprite('wall.jpg',75,150,400,100)
wall_2 = GameSprite('wall.jpg',200,90,100,400)
wall_3 = GameSprite('wall.jpg',75,150,400,100)
wall_4 = GameSprite('wall.jpg',75,150,400,100)
wall_5 = GameSprite('wall.jpg',75,200,400,100)
barriers.add(wall_1)
barriers.add(wall_2)
barriers.add(wall_3)
barriers.add(wall_4)
barriers.add(wall_5)
window = display.set_mode((700,500))
display.set_caption('Лабиринт')
picture = transform.scale(image.load('pick.jpg'), (width,height))
run = True
finish = False
back = (255,255,255)
#mixer.music.load('back.mp3')
#mixer.music.play()
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_a:
                zombi.x_speed = -5
            elif e.key == K_d:
                zombi.x_speed = 5
            elif e.key == K_w:
                zombi.y_speed = -5
            elif e.key == K_s:
                zombi.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_a:
                zombi.x_speed = 0
            elif e.key == K_d:
                zombi.x_speed = 0
            elif e.key == K_w:
                zombi.y_speed = 0
            elif e.key == K_s:
                zombi.y_speed = 0
    if not finish:
        window.fill(back)
        window.blit(picture,(0,0))
        zombi.reset()
        circle.reset()
        barriers.draw(window)
        circle.update()
        zombi.update()
        if sprite.collide_rect(zombi, circle):
            img = image.load('gameover.png')
            window.blit(transform.scale(img, (width, height)), (0, 0))
            finish = True
    display.update()



            