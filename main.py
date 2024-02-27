# Import the pygame library and initialise the game engine
import pygame
import random
pygame.init()

# Open a new window, captian it "Pong"
screen = pygame.display.set_mode ((700,500))
pygame.display.set_caption("Pong")

# here's the variable that runs our game loop
doExit = False

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#variables to hold paddle position        
#these go above game loop 
p1x = 340       
p1y = 460
p1Score = 0

#ball variables
bx = 350 #xposition
by = 250 #yposition

bVx = 5 #x velocity (horizontal speed)
bVy = 5 #y velocity (vetical speed)

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100, 250),random.randrange(100,250), random.randrange(100, 250))
        self.isDead = False
    def draw(self):
        if not self.isDead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50)) # Width and height are 100 and 50
        
    def collide(self, ball_x, ball_y):
        if not self.isDead:
            if (ball_x + 20 > self.xpos and
                ball_x < self.xpos + 100 and # Width of brick is 100
                ball_y + 20 > self.ypos and
                ball_y < self.ypos + 50):    # Height of brick is 50
                self.isDead = True
                return True
        return False
        
b1 = brick(55, 50)
b2 = brick(165, 50)
b3 = brick(274, 50)
b4 = brick(385, 50)
b5 = brick(495, 50)
b6 = brick(55, 110)
b7 = brick(165, 110)
b8 = brick(274, 110)
b9 = brick(385, 110)
b10 = brick(495, 110)
      
while not doExit: #GAME LOOP------------------------------------
    #ball movement
    bx += bVx
    by += bVy
    
    #reflect ball off side walls of sceen, change score
    if bx < 0 or bx + 20 > 700:
        bVx *= -1    
    if by < 0 or by + 20 > 500:
        bVy *= -1
    
    # Ball collision with each brick
    if b1.collide(bx, by):
        bVy *= -1
    if b2.collide(bx, by):
        bVy *= -1
    if b3.collide(bx, by):
        bVy *= -1
    if b4.collide(bx, by):
        bVy *= -1
    if b5.collide(bx, by):
        bVy *= -1
    if b6.collide(bx, by):
        bVy *= -1
    if b7.collide(bx, by):
        bVy *= -1
    if b8.collide(bx, by):
        bVy *= -1
    if b9.collide(bx, by):
        bVy *= -1
    if b10.collide(bx, by):
        bVy *= -1
        
    # event queue stuff---------------------
    clock.tick(60) #set the FPS
    
    for event in pygame.event.get(): #check if user did something
        if event.type == pygame.QUIT: #chrck if user clicked close
            doExit = True # Flag that we are done so we exit game loop
                 #game logic-------------------
    keys = pygame.key.get_pressed()      
    if keys[pygame.K_LEFT]:
         p1x-=5
    if keys[pygame.K_RIGHT]:
         p1x+=5
    
    #ball-paddle reflection
    if bx < p1x + 150 and by + 20 > p1y and by < p1y + 20:
        bVy *= -1
         
              
    #render section will go here----------------
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 150, 15), )
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()
 
    #draw a line down he middle
    pygame.draw.circle(screen, (200, 200, 0), (bx, by), 10)
    #update the screen
    pygame.display.flip()
    
     #display scores
    font = pygame.font.Font(None, 74) #use default font
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (250, 10))
    
#END GAME LOOP---------------------------------------------------------
            
pygame.quit()#when game is done close down pygame 

