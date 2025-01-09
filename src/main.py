import pygame



class Pieces:
    position:list[2] #Firs position x coordinate, second position y coordinate.
    kind:int
    color:str 
    movements=[[[(0,1),(-1,1),(1,1),(0,2)],1], #Movements of kind 0:pawn
               [[(0,1),(1,0),(0,-1),(-1,0)],7], #Movements of kind 1: Rook
               [[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)],1],#Movements of kind 2: Knight
               [[(1,1),(-1,1),(-1,-1),(1,-1)],7],#Movements of kind 3: Bishop
               [[(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)],7],#Movements of kind 4:Queen
               [[(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)],1],#Movements of kind 5: King


               ]
    

def create_piece (position:list[2],color,kind):
    piece=Pieces()
    piece.position = position
    piece.kind=kind
    piece.color=color
def init_board(grid:list(list())):
    for col_index in range(8):
        grid[1][col_index]=create_piece([0,col_index],'w',0)
        grid[6][col_index]=create_piece([6,col_index],'b',0)

    grid[0][0]=create_piece([0,0],'w',1)# Create the rooks 
    grid[0][7]=create_piece([0,7],'w',1)# Create the rooks 
    grid[7][7]=create_piece([7,7],'b',1)# Create the rooks 
    grid[7][0]=create_piece([7,0],'b',1)# Create the rooks 

    grid[0][1]=create_piece([0,1],'w',2)# Create the knights
    grid[0][6]=create_piece([0,6],'w',2)# Create the knights
    grid[7][6]=create_piece([7,6],'b',2)# Create the knights
    grid[7][1]=create_piece([7,1],'b',2)# Create the knights

    grid[0][2]=create_piece([0,2],'w',3)# Create the bishops
    grid[0][5]=create_piece([0,5],'w',3)# Create the bishops
    grid[7][5]=create_piece([7,5],'b',3)# Create the bishops
    grid[7][2]=create_piece([7,2],'b',3)# Create the bishops

    grid[0][3]=create_piece([0,3],'w',4)# Create the Queens
    grid[7][3]=create_piece([7,3],'b',4)# Create the Queens

    grid[0][4]=create_piece([0,4],'w',5)# Create the Kings
    grid[7][4]=create_piece([0,4],'w',5)# Create the Kings
    



        

    

