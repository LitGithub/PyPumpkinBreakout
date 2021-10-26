import pygame as pp
import math
pp.init()
screen = pp.display.set_mode((800, 800))
pp.display.set_caption("breakout!")
clock = pp.time.Clock()

exit = False

class pumpkin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xVel = -1
        self.yVel = 1
        self.dead = False
    def collide(self, x, y):
        return 60 > math.sqrt(math.pow((x - self.x), 2) + math.pow((y - self.y), 2))
    def draw(self):
        pp.draw.circle(screen, (255, 100, 5), (self.x, self.y), 30)
    def kill(self):
        self.dead = True
    def isDead(self):
        return self.dead

class ball:
     def __init__(self, x, y):
         self.x = x
         self.y = y
         self.xVel = 5
         self.yVel = 5
         self.dead = False
     def move(self):
        self.x = self.x + self.xVel
        self.y = self.y + self.yVel
        if self.x > 800 or self.x < 0:
            self.xVel *= -1
        if self.y < 0:
            self.yVel *= -1
        if self.y > 800:
            self.dead = True
     def reflect(self):
         self.yVel *= -1
     def draw(self):
        pp.draw.circle(screen, (255, 125, 5), (self.x, self.y), 30)
     def getX(self):
         return self.x
     def getY(self):
         return self.y
     def isDead(self):
         return self.dead
b = ball(500, 400)
bricks = []
for x in range (3):
    for i in range(7):
        bricks.append(pumpkin(int(i) * 100 + 75, int(x) * 80 + 45))

paddleX = 275
paddleY = 700

while not exit:
    clock.tick(60)
    for event in pp.event.get():
        if event.type == pp.QUIT:
            exit = True
    keys = pp.key.get_pressed()
    if keys[pp.K_LEFT]:
        paddleX-=10
    if keys[pp.K_RIGHT]:
        paddleX+=10
    if not b.isDead():
        b.move()
    if b.getX() > paddleX and b.getX() < paddleX + 200 and b.getY() + 30 > 700 and  b.getY() < 750:
        b.reflect()
    for x in bricks:
        if x.collide(b.getX(), b.getY()):
            x.kill()
            b.reflect()
    screen.fill((0,0,0))
    pp.draw.rect(screen, (0, 0, 255), (paddleX, paddleY, 200, 50))
    for x in bricks:
        x.draw()
    b.draw()
    pp.display.flip()
    for x in bricks:
        if x.isDead():
            bricks.remove(x)
