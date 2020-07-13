import pygame




def checkempty(board):
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j]== 0: 
                return True
    return False

def rowchecknum(board,row,inputnum):
        for j in range(len(board[row][j])):
            if inputnum==board[row,j]:
               return True
        return False

def colchecknum(board,col,inputnum):
    for i in range(len(board[i][col])):
        if board[i][col] == inputnum:
            return True
    return False 

def main():
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
    win=pygame.display.set_mode((500,500))
    pygame.display.set_caption('Sudoku')
    x=50
    y=50
    width=40
    height=60
    vel=5
    toggle = True
    while toggle:
        pygame.time.delay(100)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x-=vel
        if keys[pygame.K_RIGHT]:
            x+=vel
        if keys[pygame.K_UP]:
            y-=vel
        if keys[pygame.K_DOWN]:
            y+=vel
        win.fill((0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                               
               toggle=False
        pygame.draw.rect(win,(255,255,0),(x,y,width,height))
        pygame.display.update()
    pygame.quit()
main()