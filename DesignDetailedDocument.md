Here I want to track the progress made. I am not tracking specific objectives jet but I want to leave what have I done in each session and day. 

## 09/01/2025: 
### Create the Pieces class: 
    The Pieces class is has the attributes: 
    -kind: which represents the type of piece it is: pawn, queen, rook ...
    -color: which represents the team it is in NOT the cell color
    -Movements: 
        Movements gathers all the possible unit(closest ) movements a piece can make in 5 arrays ordered based on the kind value, 0-pawn, 1-rook... of 2 elements each where the second element tells what is the maximum number of movements move can make per turn. (The specific rules like peasant, or castling are not yet thought out )
## 10/01/2025
### Define the create_piece function: 
Takes the position attribute as a [y,x] list between [0,0] and [7,7] , the color as a string ('w'/'b') and the kind as 
    an integer ranging from 0-5.
    The function verifies that the parameters are within the valid range and then it creates a Pieces object called piece which is assigned each 
    parameter with the same name. Moreover piece.movements is delimited to the specific valid movements of the piece kind. 
    It finally returns the piece created. 
### Define and improve the init_board function:
NOTE: GRID[Y][X] coordinates

    It first creates an empty 8x8 grid with the List comprehensions(Investigate further). 
    Init-board then iterates from 0 to 8 and places pawns in the [1] or [6] row and the i th column. 
    After iterating throguh the pawns, it places the rest of the pieces similarly but manually. (I there are better ways I haven't thought of them)
    It finally returns the grid. 

#### Problems: 
The fact that the position is given in (y,x) gave problems assigning the positions of the chess pieces. 

### Define draw_board(grid,screen)
The draw_board function uses pygame to draw an 8x8 chess board game on a white surface. The board is not great as it does not have a border and it probably does not work properly, more testing has to be done. 
The drawing iterates over an 8 length range and then over the even numbers of \[0-8). However since the board has a diagonal pattern there is an offset that changes every row, making some rect blocks in \[0,2,4,6] and others in \[1,3,5,7]
The function is also not finished because I would like to add the pieces icon in the rect objects somehow. Currently I am investigating the pygame Sprite. 

### Define valid_movements(grid,piece):

    Valid movements returns a list of all the legal movements a piece save kings and pawns can make in the specific state of the board.

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




## 13/01/2025
### Define pawn's valid movements: 
The pawns valid movements is a decision tree where we check all the possible movements for a pawn. So long as it is not en peassant ( still workign on it). 
It first checks the color of the pawn, and from there whether it can take any piece, finally if it can move forward at all, 1 or 2 tiles. 
