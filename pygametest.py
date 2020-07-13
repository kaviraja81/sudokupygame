import pygame


class Sudoku_board:
    def __init__(self,x,y,width,height,vel,board):
        self.x=x
        self.y=y
        self.width=width    
        self.height=height
        self.vel=vel
        self.board=board
        font = pygame.font.Font('freesansbold.ttf', 30)

    def draw_rect(self):
          
        for j in range(9):
            for i in range(9): 
                
                pygame.draw.rect(win,(255,255,255),(self.x,self.y,self.width,self.height))
                if self.board[i][j] != 0 :
                    font = pygame.font.Font('freesansbold.ttf', 20)
                    message=font.render(str(self.board[i][j]),True,(0,0,255))
                    win.blit(message,(self.x+10,self.y+10))   
                self.x+=self.width
            self.x=25
            self.y+=self.height
    
    def draw_lines(self):
            # Vertical lines for the Sudoku Grid
       
        for i in range(10):
            if ( i% 3 )== 0 :
               thick=4
            else :
                thick = 1
            
            pygame.draw.line(win,(255,0,0),(s1.x,s1.y-2),(s1.x,s1.y+(9*s1.height)),thick)  #  vertical line 
            s1.x+=s1.width
                
        self.x=25
        self.y=25

        # Horizontal lines on the Sudoku Grid        
        for i in range(10):
            if (i % 3 ) == 0 :
                thick=4
            else :
                thick=1
            pygame.draw.line(win,(255,0,0),(s1.x,s1.y-2),(s1.x +(9*s1.width),s1.y-2),thick)       # horizontal line 
            s1.y+=s1.height


pygame.init()     
pygame.font.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption('Sudoku') 
toggle = True
FPS=60
clock=pygame.time.Clock()
board = [ [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ] 
while toggle:
    clock.tick(FPS)
    s1=Sudoku_board(25,25,50,30,5,board)
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
        if event.type == pygame.MOUSEBUTTONDOWN : 
            pos=pygame.mouse.get_pos()
            print(pos)
        
    pygame.draw.line(win,(255,0,0),(s1.x,s1.y-2),(s1.x +(3*s1.width),s1.y-2))
   # Rectangle for all boxes  
    s1.draw_rect()
    s1=Sudoku_board(25,25,50,30,5,board)
    s1.draw_lines()
    pygame.display.update()
pygame.quit()
