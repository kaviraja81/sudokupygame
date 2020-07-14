import pygame
import copy

class Sudoku_board:
    def __init__(self,x,y,width,height,vel,board):
        self.x=x
        self.y=y
        self.width=width    
        self.height=height
        self.vel=vel
        self.board=board
        self.selectval=[]
        font = pygame.font.Font('freesansbold.ttf', 30)
        self.updatedboard=copy.deepcopy(board)
    
    def draw_rect(self,win):
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
    
    def draw_lines(self,win):
            # Vertical lines for the Sudoku Grid
        self.x=25
        self.y=25
        for i in range(10):
            if ( i% 3 )== 0 :
               thick=4
            else :
                thick = 1
            
            pygame.draw.line(win,(255,0,0),(self.x,self.y-2),(self.x,self.y+(9*self.height)),thick)  #  vertical line 
            self.x+=self.width
                
        self.x=25
        self.y=25

        # Horizontal lines on the Sudoku Grid        
        for i in range(10):
            if (i % 3 ) == 0 :
                thick=4
            else :
                thick=1
            pygame.draw.line(win,(255,0,0),(self.x,self.y-2),(self.x +(9*self.width),self.y-2),thick)       # horizontal line 
            self.y+=self.height

    # Get the rectangle for the mouse position clicked.
    def get_rect(self,pos): 
        self.x=25
        self.y=25
        row=(pos[0]-self.x)//self.width
        col=(pos[1]-self.y)//self.height
        return [row,col]

    def write_num(self,win,key):
        x=25+(self.selectval[0]*self.width)
        y=25+(self.selectval[1]*self.height)
        #print(x,y)
        row=self.selectval[0]
        col=self.selectval[1]
        print(row,col)
        print(self.updatedboard)
        self.updatedboard[row][col]=key
        font = pygame.font.Font('freesansbold.ttf', 15)
        message=font.render(str(key),True,(128,128,128))
        
        win.blit(message,(x+5,y+5))   
        
    def clearval(self,win,board):
        row=self.selectval[0]
        col=self.selectval[1]
        print ("inside function", board[row][col])
        if board[row][col] !=0 :
           return
        x=25+(self.selectval[0]*self.width)
        y=25+(self.selectval[1]*self.height)
        self.updatedboard[row][col]=0
        pygame.draw.rect(win,(255,255,255),(x+2,y+2,30,20))

    def board_select(self,clickedcell):
        row=clickedcell[0]
        col=clickedcell[1]
        # print(row,col)
        # print(self.updatedselectboard)
        # for i in range(9):
        #     for j in range(9):
        #         self.updatedselectboard[i][j] = False
        # self.updatedselectboard[row][col]=True
        self.selectval=[row,col]
        # print(self.selectval)
def main():
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
    s1=Sudoku_board(25,25,50,30,5,board)
    s1.draw_rect(win)
    s1.draw_lines(win)
    pygame.display.update()
    while toggle:
        key=None
        clickedcell = None
        clock.tick(FPS)
        pygame.time.delay(100)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                               
                toggle=False
            if event.type == pygame.MOUSEBUTTONDOWN : 
                pos=pygame.mouse.get_pos()
                clickedcell=s1.get_rect(pos)
                print(pos,clickedcell)
                s1.board_select(clickedcell)
                print(s1.selectval)
 
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                keys=pygame.key.get_pressed()
                if keys[pygame.K_1] :
                    key=1
                if keys[pygame.K_2] :
                    key=2
                if keys[pygame.K_3] :
                    key=3
                if keys[pygame.K_4]:
                    key=4
                if keys[pygame.K_5] :
                    key=5
                if keys[pygame.K_6] :
                    key=6
                if keys[pygame.K_7]:
                    key=7
                if keys[pygame.K_8] :
                    key=8
                if keys[pygame.K_9]:
                    key=9
                if keys[pygame.K_DELETE]:
                   s1.clearval(win,board)

        if s1.selectval: 
            row=s1.selectval[0]
            col=s1.selectval[1]
       
        if key != None and board[row][col] == 0 :          
            print (key)
            print(s1.updatedboard[row][col],board[row][col])
            s1.write_num(win,key)
            print(s1.updatedboard[row][col],board[row][col])
        pygame.display.update()
main()
pygame.quit()
