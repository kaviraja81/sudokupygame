import pygame


class Sudoku_board:
    def __init__(self,x,y,width,height,vel):
        self.x=x
        self.y=y
        self.width=width    
        self.height=height
        self.vel=vel
        

pygame.init()     

win=pygame.display.set_mode((500,500))
pygame.display.set_caption('Sudoku') 
toggle = True

while toggle:
    s1=Sudoku_board(25,25,50,30,5)
    pygame.time.delay(100)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and s1.x > s1.vel:
        s1.x-=s1.vel
    if keys[pygame.K_RIGHT] and s1.x < 500-s1.width-s1.vel:
        s1.x+=s1.vel
    if keys[pygame.K_UP] and s1.y > s1.vel:
        s1.y-=s1.vel
    if keys[pygame.K_DOWN] and s1.y < 500-s1.height-s1.vel:
        s1.y+=s1.vel
    win.fill((0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                               
            toggle=False
    pygame.draw.line(win,(255,0,0),(s1.x,s1.y-2),(s1.x +(3*s1.width),s1.y-2))
   
    # Rectangle for 1 box  
    for j in range(9):
        for i in range(9): 
            pygame.draw.rect(win,(255,255,255),(s1.x,s1.y,s1.width,s1.height))
            s1.x+=s1.width
        s1.x=25
        s1.y+=s1.height
    
    # Vertical lines for the Sudoku Grid
  
    s1=Sudoku_board(25,25,50,30,5)
    for i in range(10):
        if ( i% 3 )== 0 :
           thick=4
        else :
           thick = 1
        
        pygame.draw.line(win,(255,0,0),(s1.x,s1.y-2),(s1.x,s1.y+(9*s1.height)),thick)  #  vertical line 
        s1.x+=s1.width
                
    s1=Sudoku_board(25,25,50,30,5)

# Horizontal lines on the Sudoku Grid        
    for i in range(10):
        if (i % 3 ) == 0 :
            thick=4
        else :
            thick=1
        pygame.draw.line(win,(255,0,0),(s1.x,s1.y-2),(s1.x +(9*s1.width),s1.y-2),thick)       # horizontal line 
        s1.y+=s1.height
    
    pygame.display.update()
pygame.quit()
