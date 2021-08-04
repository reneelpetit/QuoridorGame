#Name: Renee Petit
#Date: 8/3/21
#Description:

class QuoridorGame():
    def __init__(self):
        """* `init` method that initializes the board with the fences (four edges) and pawns (P1 and P2) placed in the correct positions. """
        return

    def move_pawn(self):
        """* `move_pawn` method takes following two parameters in order: an integer that represents which player (1 or 2) is making the move and a tuple with the coordinates of where the pawn is going to be moved to.
            - if the move is forbidden by the rule or blocked by the fence, return `False`
            - if the move was successful or if the move makes the player win, return `True`
            - if the game has been already won, return `False`"""
        return

    def place_fence(self):
        """* `place_fence` method takes following parameters in order: an integer that represents which player (1 or 2) is making the move, a letter indicating whether it is vertical (v) or horizontal (h) fence, a tuple of integers that represents the position on which the fence is to be placed.   
            - if player has no fence left, or if the fence is out of the boundaries of the board, or if there is already a fence there and the new fence will overlap or intersect with the existing fence, return `False`. 
            - If the fence can be placed, return `True`.
            - If it breaks the fair-play rule (and if you are doing the extra credit part), return exactly the string `breaks the fair play rule`.
            - If the game has been already won, return `False`"""
        return
    
    def is_winnter(self):
        """* `is_winner` method that takes a single integer representing the player number as a parameter and returns `True` if that player has won and `False` if that player has not won."""
        return
    
    def print_board(self):
        """* You might also find implementing a `print_board` method useful to print the board to the screen. It's not required that you implement this method. """
        return