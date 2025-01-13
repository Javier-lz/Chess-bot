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
    history=0
    movements=[[[(1,0),(-1,1),(1,1),(-1,-1),(1,-1),(-1,0),(2,0),(-2,0)],2], #Movements of kind 0:pawn
               [[(0,1),(1,0),(0,-1),(-1,0)],8], #Movements of kind 1: Rook
               [[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)],2],#Movements of kind 2: Knight
               [[(1,1),(-1,1),(-1,-1),(1,-1)],8],#Movements of kind 3: Bishop
               [[(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)],8],#Movements of kind 4:Queen
               [[(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)],2],#Movements of kind 5: King


               ]
    def __repr__(self):
        return 'piece {} {}'.format(self.kind, self.color)
    


def draw_board(board:list[list[8]],screen):#TODO
    """
    The function draw board uses pygame to display a chess board. For now it is just 
    """
    block_size=SIZE_BLOCK
    
    offset=1
    
    for i in range(0,8):

        for j in range(0,8,2):
            rect=pygame.Rect(START_WIDTH+(j+offset)*block_size,START_HEIGHT+ i*block_size,block_size,block_size)
            
            pygame.draw.rect(screen,BLACK,rect)
        if offset==1:
            offset=0
        else:
            offset =1


def check_validity(kind,color,position):
    if kind not in range(6):
        print("The kind value is not valid it is not in ", range(6))
        raise ValueError
    if color not in ['w','b']:
        print("The kind value is not valid it is not in ", range(6))
        raise ValueError
    if 0>position[0]>=8 | 0>position[1]>=8:
        print("The position value is not valid it is not in ", range(8))
        raise ValueError
    

def create_piece (position:list[2],color,kind) -> Pieces:
    """
    Takes the position attribute as a [y,x] list between [0,0] and [7,7] , the color as a string ('w'/'b') and the kind as 
    an integer ranging from 0-5.
    The function verifies that the parameters are within the valid range and then it creates a Pieces object called piece which is assigned each 
    parameter with the same name. Moreover piece.movements is delimited to the specific valid movements of the piece kind. 
    It finally returns the piece created. 
    """
    check_validity(kind,color,position)



    piece=Pieces()
    piece.position = position
    piece.kind=kind
    piece.color=color
    piece.movements= piece.movements[kind]
    return piece
def init_board(): 
    """
    NOTE: board[Y][X] coordinates

    It first creates an empty 8x8 board with the List comprehensions(Investigate further). 
    Init-board then iterates from 0 to 8 and places pawns in the [1] or [6] row and the i th column. 
    After iterating throguh the pawns, it places the rest of the pieces similarly but manually. (I there are better ways I haven't thought of them)
    It finally returns the board. 
    """
    board =[[0 for _ in range(8)] for _ in range(8)]
    print(board)
    
    for  i in range(8):
        board[1][i]=create_piece([1,i],'w',0)
        board[6][i]=create_piece([6,i],'b',0)
    print(board[3][0]==0)

    board[0][0]=create_piece([0,0],'w',1)# Create the rooks 
    board[0][7]=create_piece([0,7],'w',1)# Create the rooks 
    board[7][7]=create_piece([7,7],'b',1)# Create the rooks 
    board[7][0]=create_piece([7,0],'b',1)# Create the rooks 

    board[0][1]=create_piece([0,1],'w',2)# Create the knights
    board[0][6]=create_piece([0,6],'w',2)# Create the knights
    board[7][6]=create_piece([7,6],'b',2)# Create the knights
    board[7][1]=create_piece([7,1],'b',2)# Create the knights

    board[0][2]=create_piece([0,2],'w',3)# Create the bishops
    board[0][5]=create_piece([0,5],'w',3)# Create the bishops
    board[7][5]=create_piece([7,5],'b',3)# Create the bishops
    board[7][2]=create_piece([7,2],'b',3)# Create the bishops

    board[0][3]=create_piece([0,3],'w',4)# Create the Queens
    board[7][3]=create_piece([7,3],'b',4)# Create the Queens

    board[0][4]=create_piece([0,4],'w',5)# Create the Kings
    board[7][4]=create_piece([0,4],'b',5)# Create the Kings
    return board
def print_board(board) -> None:
    """
    The function print_board iterates through a two dimension list and prints the elements by rows. 
    """
    if board:
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j],'--', end='')
            print()

def king_movements(king):
    pass


def pawn_movements(board,pawn):
    sol=[]
    y,x=pawn.position

    

    if pawn.color =='b':
    
        if 0<=x-1 <8 and 0<=y-1 <8 :
            if board[y-1][x-1] != 0:
                if board[y-1][x-1].color =='w':
                    sol.append((-1,-1))
        if 0<=x+1<8 and 0<=y-1<8:
             if board[y-1][x+1] != 0:
                if board[y-1][x+1].color =='w':
                    sol.append((-1,-1))

        if 0<=x <8 and 0<=y-1<8:
            if board[y-1][x] ==0:
                sol.append((-1,0))
                if pawn.history == 0 and 0<=y-2 <8 and board[y-2][x]==0:
                    sol.append((-2,0))
    elif pawn.color =='w':
    
        if 0<=x-1 <8 and 0<=y+1 <8 :
            if board[y+1][x-1] != 0:
                if board[y+1][x-1].color =='b':
                    sol.append((1,-1))
        if 0<=x+1<8 and 0<=y+1<8:
             if board[y+1][x+1] != 0:
                if board[y+1][x+1].color =='b':
                    sol.append((1,1))

        if 0<=x <8 and 0<=y+1<8:
            if board[y+1][x] ==0:
                sol.append((1,0))
                if pawn.history == 0 and 0<=y+2 <8 and board[y+2][x]==0:
                    sol.append((2,0))
    

    
    return sol
                




def valid_movements(board,piece:Pieces) -> list:
    """
    valid movements returns a list of all the legal movements a piece save kings and pawns can make in the specific state of the board.

    It receives the state of the board and the piece that we want to move. Then it checks if the piece is valid except for the position because the position will be out of 
    range when we want to terminate. Similarly to a depth first search algorithm. 

    For each piece it starts iterating over the possible movements which are movements[0]. These represent a kinght's l shape movement, the bishop's diagonal ... It makes one movement
    at a time. The number of times the piece does a movements is limited by the type of piece. If they can move limitlessly then they will have a 8 times iterator, for example
    queens and rooks, however if they can only move once in a direction like the knight the top will be 2 , because python's range is up to but not including. 
    If a movement is  valid  aka it is either an empty square then it continues to the next. 
    The base cases are
    If it's out of bounds then it will end the loop for that move direction. 
    If it's within bounds and reach a piece whose color is different than the piece parameter then that position is added but break afterwards. 
    Finally if it's a piece of it's own color then it stops that direction. 


    

    """
    check_validity(piece.kind,piece.color,position=[0,0])
    if piece.kind==5:
        return king_movements()
    elif piece.kind==0:
        return pawn_movements(board,piece)
        
    y,x=piece.position
    sol=[]
    movements=piece.movements

    for move in movements[0]:
        for i in range(1,movements[1]):
            mov_x=x+i*move[1]
            mov_y=y+i*move[0]
            if (0<=mov_x <8) & (0<= mov_y<8): # Check we are still in the board
                if board[mov_y][mov_x] ==0:
                    sol.append([mov_y,mov_x])
                
                elif board[mov_y][mov_x].color != piece.color:
                    sol.append([mov_y,mov_x])
                    break
                else:
                    break
            else:
                break
                

    return sol


def movable_pieces(board,color):
    color_pieces=[]
    index=0
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] != 0):
                if(board[i][j].color ==color):
                    color_pieces.append(board[i][j])
                    index+=1
    return color_pieces

def make_move(board,turn_color,playing:int):
    list_move_pieces= movable_pieces(board,turn_color)
    for index,i in enumerate(list_move_pieces):
        print(i, i.position , index)
    print_board(board)
    choice=int(input(" \n \n \n What piece do you want to move, choose the index : "))
    
    option,piece = valid_movements(board,list_move_pieces[choice]),list_move_pieces[choice]
    while not option: 
        
        print_board(board)
        print(list_move_pieces)
        choice=int(input("What piece do you want to move, choose the index : \n \n \n"))
        option,piece = valid_movements(board,list_move_pieces[choice]),list_move_pieces[choice]
        list_move_pieces.pop(choice)
        if not list_move_pieces:
            playing=0
            print("You have no possible moves it is a draw")

    print_board(board)
    print(option)
    print(piece.position)
    move_choice = int(input("Choose what movement you want to make \n \n \n "))
    
    #board[piece.position[0]][piece.position[1]],board[option[move_choice][0]][option[move_choice][1]] =0,board[piece.position[0]][piece.position[1]]
    # Step 1: Store the value of the piece in a temporary variable
    temp = board[piece.position[0]][piece.position[1]]

    # Step 2: Update the board positions
    board[piece.position[0]][piece.position[1]] = 0
    board[piece.position[0]+option[move_choice][0]][piece.position[1]+option[move_choice][1]] = temp
    
    piece.position=[option[move_choice][0],option[move_choice][1]]
    piece.history+=1
    
    print(board[piece.position[0]][piece.position[1]])
    if turn_color =='b':
        return 'w'
    else:
        return 'b'

   
    

def choose_move():
    pass
def play(board):
    turn_color = 'b' #Current color that moves. 
    playing=1
    #draw_board(board) when draw board works correctly
    while playing:
        turn_color=make_move(board,turn_color,playing)


        
        
        
        
            

   

def main():
   #pygame.init()
   #SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
   #SCREEN.fill(WHITE)
    board=init_board()
    print_board(board)
    play(board)

    #while True: 
    #    draw_board(board,SCREEN)
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            pygame.quit()
    #            exit()
    #    pygame.display.update()

    

    

if __name__=="__main__":
    main()


    

        

    

