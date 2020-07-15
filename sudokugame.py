import pygame
import copy
import ruleschk

class Sudoku_board:
    def __init__(self,x,y,width,height,vel,board):
        self.x=x
        self.y=y
        self.width=width    
        self.height=height
        self.vel=vel
        self.board=board
        self.row=0
        self.col=0
        self.strike=0
       
        self.tempboard=copy.deepcopy(board)
        self.updatedboard=copy.deepcopy(board)
    
    '''### This function is used to draw rectangles for the Sudoku Board
    '''
    def draw_rect(self,win):
        win.fill((255,255,255))
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
    '''
    ## This function is used to draw grid lines on the board. The logic is included to have thick lines on the box and 
    # thinner lines on the other boxes 
    '''
    def draw_lines(self,win):
            # Vertical lines for the Sudoku Grid
        self.x=25
        self.y=25
        for i in range(10):
            if ( i% 3 )== 0 :
               thick=4
            else :
                thick = 1
            
            pygame.draw.line(win,(0,0,0),(self.x,self.y-2),(self.x,self.y+(9*self.height)),thick)  #  vertical line 
            self.x+=self.width
                
        self.x=25
        self.y=25

        # Horizontal lines on the Sudoku Grid        
        for i in range(10):
            if (i % 3 ) == 0 :
                thick=4
            else :
                thick=1
            pygame.draw.line(win,(0,0,0),(self.x,self.y-2),(self.x +(9*self.width),self.y-2),thick)       # horizontal line 
            self.y+=self.height

    '''' Find the position of the rectangle box that was clicked in the mouse 
    '''
    # Get the rectangle for the mouse position clicked.
    def get_rect(self,pos): 
        self.x=25
        self.y=25
        row=(pos[0]-self.x)//self.width
        col=(pos[1]-self.y)//self.height
        return [row,col]

    ''' Write numbers on the board  . Initially when the numbers are written as a trial, it is written in grey colour 
        and the valid variable is set to False. (Else logic)
        When the number is written adn enter is pressed on the keyboard, if hte number is valid, the function 
        is called to write it on the board and the colour of the number is black. The updatedboard variable is set to the 
        number and the tempboard is set back to zero.
    '''
    def write_num(self,win,key,valid):

        x=25+(self.row*self.width)
        y=25+(self.col*self.height)
        if valid : 
           self.updatedboard[self.row][self.col]=key
           self.tempboard[self.row][self.col]=0
           font = pygame.font.Font('freesansbold.ttf', 20)
           message=font.render(str(self.updatedboard[self.row][self.col]),True,(0,0,0))
           win.blit(message,(x+10,y+10)) 
        else :    
           self.tempboard[self.row][self.col]=key
           font = pygame.font.Font('freesansbold.ttf', 15)
           message=font.render(str(key),True,(128,128,128))
           win.blit(message,(x+5,y+5))   
   
    
    '''
        This function @clearval is used to clear the number on the board, 
        This function is called in  case of delete or writing a valid number after pressing enter on the keyboard
    '''
    def clearval(self,win,board):
        if board[self.row][self.col] !=0 :
           return
        x=25+(self.row*self.width)
        y=25+(self.col*self.height)
        self.tempboard[self.row][self.col]=0
        pygame.draw.rect(win,(255,255,255),(x+2,y+2,30,20))

    ''' This function is called to set the row and col variable in the object to the clicked mouse position
    '''
    def board_select(self,clickedcell):
        self.row=clickedcell[0]
        self.col=clickedcell[1]
 
    ''' Validate function is used to call the ruleschk module to check 
        if the number is not present in the Row using rowchknum function , 
        if the number is not present in the column using colchknum function
        if the number is not prsent in the box using boxchknum function. 
        If the number is not present then the number is a valid numbe Hence this function returns True 
        else it returns False 
    '''
    def validate(self): 
        if ruleschk.rowchecknum(self.updatedboard,self.row,self.tempboard[self.row][self.col]) and      \
           ruleschk.colchecknum(self.updatedboard,self.col,self.tempboard[self.row][self.col]) :
           if ruleschk.boxcheck(self.updatedboard,self.row,self.col,self.tempboard[self.row][self.col]):
              return True
           else :
              return False  
        else :
            return False

    '''Put an X when a wrong number is entered'''

    def wrongnum_notify(self,win):
        self.strike+=1
        font = pygame.font.Font('freesansbold.ttf', 15)
        message=font.render("X " *self.strike,True,(255,0,0))
        win.blit(message,(25,300))   
    
    '''Complete the sudoku game''' 
    def finishedmessage(self,win):
        font = pygame.font.Font('freesansbold.ttf', 15)
        message=font.render(" Success . You won the game" ,True,(0,255,0))
        win.blit(message,(25,325))   
    
def main():
    pygame.init()     
    pygame.font.init()
    win=pygame.display.set_mode((500,350))
    pygame.display.set_caption('Sudoku') 
    toggle = True
    FPS=60
    clock=pygame.time.Clock()
   
    pygame.display.update()
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

    ###Get details of the mouse position only if it is inside the board 
                if pos[0]>=25 and pos[0] <= 475 and pos[1]>=25 and pos[1]<=295 :
                    clickedcell=s1.get_rect(pos)
                    s1.board_select(clickedcell)
               
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
                if keys[pygame.K_RETURN]:
                   if s1.updatedboard[s1.row][s1.col] == 0 :
                      valid = False 
                      valid = s1.validate() 
                      if pos[0]>=25 and pos[0] <= 475 and pos[1]>=25 and pos[1]<=295:
                        if valid:
                            keyval=s1.tempboard[s1.row][s1.col]
                            s1.clearval(win,board)
                            s1.write_num(win,keyval,valid)
                #Check if there are empty fields to be written. If the board is empty 
                # Print on  the board with a success message
                            if  not ruleschk.checkempty(s1.updatedboard):
                                s1.finishedmessage(win)
                                
                        else : 
                            s1.clearval(win,board)
                            s1.wrongnum_notify(win)
                        
        
        if key != None and s1.updatedboard[s1.row][s1.col] == 0 : 
           s1.clearval(win,board)
           valid=False
           s1.write_num(win,key,valid)
        pygame.display.update()
main()
pygame.quit()
