
def checkempty(board):
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j]== 0: 
                return True
    return False

def rowchecknum(board,row,inputnum):

        for j in range(len(board)):
            if inputnum==board[row][j]:
               return False
        return True

def colchecknum(board,col,inputnum):
    for i in range(len(board[0])) :
        if board[i][col] == inputnum:
            return False
    return True

def boxcheck(board,row,col,inputnum):
    if row % 3 == 0 :
       boxrow = row 
    else :
        boxrow= row- (row%3)
    
    if col % 3 == 0 :
       boxcol=col
    else : 
        boxcol=col-(col%3)
 
    
    for i in range(3):
       for j in range(3):
           if board[boxrow][boxcol] == inputnum :
                return False
                boxcol+=1
       boxrow+=1
    return True  



 