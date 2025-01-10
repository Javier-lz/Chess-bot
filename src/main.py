import pygame


WIDTH=800
HEIGHT = 800
SIZE_BLOCK=60
BLACK = (100,10,10)
WHITE=(255,255,255)
START_WIDTH= (800-SIZE_BLOCK*8)/2
START_HEIGHT=START_WIDTH


class Pieces:
    position:list[2] #FIRST Y THEN X coordinate
    kind:int
    color:str 
    movements=[[[(0,1),(-1,1),(1,1),(0,2)],2], #Movements of kind 0:pawn
               [[(0,1),(1,0),(0,-1),(-1,0)],8], #Movements of kind 1: Rook
               [[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)],2],#Movements of kind 2: Knight
               [[(1,1),(-1,1),(-1,-1),(1,-1)],8],#Movements of kind 3: Bishop
               [[(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)],8],#Movements of kind 4:Queen
               [[(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)],2],#Movements of kind 5: King


               ]
    def __repr__(self):
        return 'piece {} {}'.format(self.kind, self.color)
    

def draw_board(grid:list[list[8]],screen):#TODO
    """
    The function draw board uses pygame to display a chess board. For now it is just 
    """
    block_size=SIZE_BLOCK
    color = [WHITE,BLACK]
    offset=1
    
    for i in range(0,8):

        for j in range(0,8,2):
            rect=pygame.Rect(START_WIDTH+(j+offset)*block_size,START_HEIGHT+ i*block_size,block_size,block_size)
            
            pygame.draw.rect(screen,BLACK,rect)
        if offset==1:
            offset=0
        else:
            offset =1

def create_piece (position:list[2],color,kind) -> Pieces:
    """
    Takes the position attribute as a [y,x] list between [0,0] and [7,7] , the color as a string ('w'/'b') and the kind as 
    an integer ranging from 0-5.
    The function verifies that the parameters are within the valid range and then it creates a Pieces object called piece which is assigned each 
    parameter with the same name. Moreover piece.movements is delimited to the specific valid movements of the piece kind. 
    It finally returns the piece created. 
    """
    if kind not in range(6):
        print("The kind value is not valid it is not in ", range(6))
        raise ValueError
    if color not in ['w','b']:
        print("The kind value is not valid it is not in ", range(6))
        raise ValueError
    if 0>position[0]>=8 | 0>position[1]>=8:
        print("The position value is not valid it is not in ", range(8))
        raise ValueError



    piece=Pieces()
    piece.position = position
    piece.kind=kind
    piece.color=color
    piece.movements= piece.movements[kind]
    return piece
def init_board(): 
    """
    NOTE: GRID[Y][X] coordinates

    It first creates an empty 8x8 grid with the List comprehensions(Investigate further). 
    Init-board then iterates from 0 to 8 and places pawns in the [1] or [6] row and the i th column. 
    After iterating throguh the pawns, it places the rest of the pieces similarly but manually. (I there are better ways I haven't thought of them)
    It finally returns the grid. 
    """
    grid =[[0 for _ in range(8)] for _ in range(8)]
    print(grid)
    
    for  i in range(8):
        grid[1][i]=create_piece([1,i],'w',0)
        grid[6][i]=create_piece([6,i],'b',0)
    print(grid[3][0]==0)

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
    return grid
def print_board(grid) -> None:
    """
    The function print_board iterates through a two dimension list and prints the elements by rows. 
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],'--', end='')
        print()



if __name__=="__main__":
    main()


    

        

    

