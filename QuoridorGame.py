#Name: Renee Petit
#Date: 8/3/21
#Description:

class QuoridorGame():
    def __init__(self):
        """* `init` method that initializes the board with the fences (four edges) and pawns (P1 and P2) placed in the correct positions. """
        self._board = {
            (0,0): [],
            (0,1): [],
            (0,2): [],
            (0,3): [],
            (0,4): [],
            (0,5): [],
            (0,6): [],
            (0,7): [],
            (0,8): [],
            (1,0): [],
            (1,1): [],
            (1,2): [],
            (1,3): [],
            (1,4): [],
            (1,5): [],
            (1,6): [],
            (1,7): [],
            (1,8): [],
            (2,0): [],
            (2,1): [],
            (2,2): [],
            (2,3): [],
            (2,4): [],
            (2,5): [],
            (2,6): [],
            (2,7): [],
            (2,8): [],
            (3,0): [],
            (3,1): [],
            (3,2): [],
            (3,3): [],
            (3,4): [],
            (3,5): [],
            (3,6): [],
            (3,7): [],
            (3,8): [],
            (4,0): [1],
            (4,1): [],
            (4,2): [],
            (4,3): [],
            (4,4): [],
            (4,5): [],
            (4,6): [],
            (4,7): [],
            (4,8): [2],
            (5,0): [],
            (5,1): [],
            (5,2): [],
            (5,3): [],
            (5,4): [],
            (5,5): [],
            (5,6): [],
            (5,7): [],
            (5,8): [],
            (6,0): [],
            (6,1): [],
            (6,2): [],
            (6,3): [],
            (6,4): [],
            (6,5): [],
            (6,6): [],
            (6,7): [],
            (6,8): [],
            (7,0): [],
            (7,1): [],
            (7,2): [],
            (7,3): [],
            (7,4): [],
            (7,5): [],
            (7,6): [],
            (7,7): [],
            (7,8): [],
            (8,0): [],
            (8,1): [],
            (8,2): [],
            (8,3): [],
            (8,4): [],
            (8,5): [],
            (8,6): [],
            (8,7): [],
            (8,8): []
                }
    
    def current_location(self, pawn):
        #method to return the current location of a pawn
        for key, value in self._board.items():
            #find where the pawn is on the board 
            if pawn in value:
                #Get the key & store key in start_coord
                start_coord = key
                print("start_coord in current location: ", start_coord)
                return start_coord
    
    def set_location(self, pawn, move_coord):
        for key, value in self._board.items():
            #find the key 
            if move_coord == key:
                #add the pawn to the value of that key
                #TO DO: don't delete any fences that are there!!!
                self._board.update({key: pawn})
    
    def get_difference_between_coords(self, pawn, current_location, move_location):
        #method to check the difference between current location and move location
        pass

    def move_pawn(self, pawn, move_coord):
        """* `move_pawn` method takes following two parameters in order: an integer that represents which player (1 or 2) is making the move and a tuple with the coordinates of where the pawn is going to be moved to.
            - if the move is forbidden by the rule or blocked by the fence, return `False`
            - if the move was successful or if the move makes the player win, return `True`
            - if the game has been already won, return `False`"""
        #check if game is already won by calling is_winner()
        if self.is_winner(pawn):
            #if True,return False
            return False
        #find the starting coordinates of the pawn by calling current_location and storing key in start_coord
        start_coord = self.current_location(pawn)
        print("move pawn start coord: ", start_coord)
        #find the distance between the start_coord and the move_coord
        difference_between_locations = self.get_difference_between_coords(pawn, start_coord, move_coord)
        print("the difference is ", difference_between_locations)
        #TO DO: if player tries to move over a fence, 
            #return false
        if move_coord[0] < 0 or move_coord[0] > 8 or move_coord[1] < 0 or move_coord[1] > 8:
            #if player tries to move off the board, 
            #return false
            return False
        #TO DO: if player tries to move to space they cannot move to,
            #return false
        #TO DO: if player tries to move to a square that already has a pawn,
        if 1 in self._board.get(move_coord) or 2 in self._board.get(move_coord):
            print("yes pawn is in the space")
            #if there is no fence,
            if 'h' in self._board.get(move_coord):
                pass
                #pawn jumps over that space to the next one
                #else move diagnol
        #TO DO: if player tries to move to a square they can move to,
            #find location of current pawn
            #set that location to empty
            #move pawn to coordinates given
    def place_fence(self, pawn, direction_of_fence, coord_to_place_fence):
        """* `place_fence` method takes following parameters in order: an integer that represents which player (1 or 2) is making the move, a letter indicating whether it is vertical (v) or horizontal (h) fence, a tuple of integers that represents the position on which the fence is to be placed.   
            - if player has no fence left, or if the fence is out of the boundaries of the board, or if there is already a fence there and the new fence will overlap or intersect with the existing fence, return `False`. 
            - If the fence can be placed, return `True`.
            - If it breaks the fair-play rule (and if you are doing the extra credit part), return exactly the string `breaks the fair play rule`.
            - If the game has been already won, return `False`"""
        #check that no one has won by calling is_winner
        if self.is_winner(pawn):
            #if True,return False
            return False
        #TO DO: check that pawn has fences left to use
            #if yes,
                #check that the fence coordinates are not out of bounds
                    #if yes,
                        #return False
                #check that there isn't already a fence
                    #if yes, 
                        #return False
                #else find the key that matches the coord_to_place_fence
                    #add the fence details to the values in the matching key
            #else no fences left, return false
    
    def is_winner(self, pawn):
        """* `is_winner` method that takes a single integer representing the player number as a parameter and returns `True` if that player has won and `False` if that player has not won."""
        #find the current location of pawn by calling current_location
        start_coords = self.current_location(pawn)
        print("is_winner start coords: ", start_coords)
        if pawn == 1:
            if start_coords[1] == 8:
                #if pawn1 is on the y coordinate 8
                print("pawn 1 is on y axis 8, win!")
                #pawn1 wins, return true
                return True
        if pawn == 2:
            if start_coords[1] == 0:
                #if pawn2 is on y coordinate 0
                print("pawn 2 is on y coord 0, win!")
                #pawn2 wins, return true
                return True
        else:
            return False
    
    def print_board(self):
        """* You might also find implementing a `print_board` method useful to print the board to the screen. It's not required that you implement this method. """
        print(self._board[(0,0)], self._board[(1,0)], self._board[(2,0)], self._board[(3,0)], self._board[(4,0)], self._board[(5,0)], self._board[(6,0)], self._board[(7,0)], self._board[(8,0)])
        print(self._board[(0,1)], self._board[(1,1)], self._board[(2,1)], self._board[(3,1)], self._board[(4,1)], self._board[(5,1)], self._board[(6,1)], self._board[(7,1)], self._board[(8,1)])
        print(self._board[(0,2)], self._board[(1,2)], self._board[(2,2)], self._board[(3,2)], self._board[(4,2)], self._board[(5,2)], self._board[(6,2)], self._board[(7,2)], self._board[(8,2)])
        print(self._board[(0,3)], self._board[(1,3)], self._board[(2,3)], self._board[(3,3)], self._board[(4,3)], self._board[(5,3)], self._board[(6,3)], self._board[(7,3)], self._board[(8,3)])
        print(self._board[(0,4)], self._board[(1,4)], self._board[(2,4)], self._board[(3,4)], self._board[(4,4)], self._board[(5,4)], self._board[(6,4)], self._board[(7,4)], self._board[(8,4)])
        print(self._board[(0,5)], self._board[(1,5)], self._board[(2,5)], self._board[(3,5)], self._board[(4,5)], self._board[(5,5)], self._board[(6,5)], self._board[(7,5)], self._board[(8,5)])
        print(self._board[(0,6)], self._board[(1,6)], self._board[(2,6)], self._board[(3,6)], self._board[(4,6)], self._board[(5,6)], self._board[(6,6)], self._board[(7,6)], self._board[(8,6)])
        print(self._board[(0,7)], self._board[(1,7)], self._board[(2,7)], self._board[(3,7)], self._board[(4,7)], self._board[(5,7)], self._board[(6,7)], self._board[(7,7)], self._board[(8,7)])
        print(self._board[(0,8)], self._board[(1,8)], self._board[(2,8)], self._board[(3,8)], self._board[(4,8)], self._board[(5,8)], self._board[(6,8)], self._board[(7,8)], self._board[(8,8)])

game = QuoridorGame()
game.print_board()
game.move_pawn(1, (4,8))
game.is_winner(1)