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






