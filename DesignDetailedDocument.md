Here I want to track the progress made. I am not tracking specific objectives jet but I want to leave what have I done in each session and day. 

## 09/01/2025: 
### Create the Pieces class: 
    The Pieces class is has the attributes: 
    -kind: which represents the type of piece it is: pawn, queen, rook ...
    -color: which represents the team it is in NOT the cell color
    -Movements: 
        Movements gathers all the possible unit(closest ) movements a piece can make in 5 arrays ordered based on the kind value, 0-pawn, 1-rook... of 2 elements each where the second element tells what is the maximum number of movements move can make per turn. (The specific rules like peasant, or castling are not yet thought out )
### Define the create_piece function: 
Takes the position attribute as a [y,x] list between [0,0] and [7,7] , the color as a string ('w'/'b') and the kind as 
    an integer ranging from 0-5.
    The function verifies that the parameters are within the valid range and then it creates a Pieces object called piece which is assigned each 
    parameter with the same name. Moreover piece.movements is delimited to the specific valid movements of the piece kind. 
    It finally returns the piece created. 
    


