#Name: Renee Petit
#Date: 8/3/21
#Description: Program to play Quoridor with 2 players who have 10 fences each.
import math

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
        self._pawn1fences = 10
        self._pawn2fences = 10
        self._turn = 1
    
    def current_location(self, pawn):
        #method to return the current location of a pawn
        for key, value in self._board.items():
            #find where the pawn is on the board 
            if pawn in value:
                #Get the key & store key in start_coord
                start_coord = key
                return start_coord
    
    def set_location_pawn(self, pawn, move_coord):
        for key, value in self._board.items():
            #find the key 
            if move_coord == key:
                new_value = [pawn] + value
                #add the pawn to the value of that key
                self._board.update({key: new_value})
                return
    
    def set_location_fence(self, fence, fence_coord):
        for key, value in self._board.items():
            #find the key 
            if fence_coord == key:
                #add the fence to the value of that key
                new_value = [fence] + value
                self._board.update({key: new_value})
                return

    def delete_current_location(self, pawn, current_location):
        for key, value in self._board.items():
            #find key
            if current_location == key:
                #remove pawn from value
                value.remove(pawn)
                #update board
                self._board.update({key: value})
                return

    def is_diagonal_allowed(self, pawn, current_location, move_location):
        #check if the requested diagnol move is allowed or not
        #check if other pawn is above the current_location
        below_coord = (current_location[0], current_location[1] + 1)
        above_coord = (current_location[0], current_location[1] - 1)
        below_fence_coord = (current_location[0], current_location[1] + 2)
        above_fence_coord = (current_location[0], current_location[1] - 2)

        if below_coord[0] > 0 and below_coord[0] < 8 and below_coord[1] > 0 and below_coord[1] < 8:
           #if below coord is inbounds    
            if (pawn == 1 and 2 in self._board.get(below_coord)) or (pawn == 2 and 1 in self._board.get(below_coord)):
                #if h 2 below our pawn's spot
                if 'h' in self._board.get(below_fence_coord):
                    #if moving down and right or down and left, return True
                    if move_location == (current_location[0] - 1, current_location[1] + 1) or move_location == (current_location[0] + 1, current_location[1] + 1):
                        #yes can move
                        self.set_location_pawn(pawn, move_location)
                        self.delete_current_location(pawn, current_location)
                        return True
        #check above
        if above_coord[0] > 0 and above_coord[0] < 8 and above_coord[1] > 0 and above_coord[1] < 8:
            #if above coord is inbounds
            if (pawn == 1 and 2 in self._board.get(above_coord)) or (pawn == 2 and 1 in self._board.get(above_coord)):
                #if h above our pawn's spot
                if 'h' in self._board.get(above_fence_coord):
                    #if moving up and right or up and left, return True
                    if move_location == (current_location[0] -1, current_location[1] - 1) or move_location == (current_location[0] + 1, current_location[1] + 1):
                        #yes can move
                        self.set_location_pawn(pawn, move_location)
                        self.delete_current_location(pawn, current_location)
                        return True      
        return False

    def difference_between_coords(self, pawn, current_location, move_location):
        #method to check the difference between current location and move location
        x1 = current_location[0]
        x2 = move_location[0]
        y1 = current_location[1]
        y2 = move_location[1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if distance != 1:
            if distance == math.sqrt(2):
                if not self.is_diagonal_allowed(pawn, current_location, move_location):
                    return False
                else:
                    return "diagonal"
            return False
        else:
            return True
    
    def is_horizontal_move(self, current_location, move_location):
        x1 = current_location[0]
        x2 = move_location[0]
        answer = x1 - x2
        if abs(answer) == 1:
            return True
        return False

    def move_pawn(self, pawn, move_coord):
        """* `move_pawn` method takes following two parameters in order: an integer that represents which player (1 or 2) is making the move and a tuple with the coordinates of where the pawn is going to be moved to.
            - if the move is forbidden by the rule or blocked by the fence, return `False`
            - if the move was successful or if the move makes the player win, return `True`
            - if the game has been already won, return `False`"""
        #check if it's the player's turn
        if self._turn != pawn:
            return False
        #check if game is already won by calling is_winner()
        if self.is_winner(pawn):
            #if True,return False
            return False
        #find the starting coordinates of the pawn by calling current_location and storing key in start_coord
        start_coord = self.current_location(pawn)
        if move_coord[0] < 0 or move_coord[0] > 8 or move_coord[1] < 0 or move_coord[1] > 8:
            #if player tries to move off the board, 
            #return false
            return False
        difference = self.difference_between_coords(pawn, start_coord, move_coord)
        #check if the distance between the start_coord and the move_coord is 1
        if difference == "diagonal":
            #update player turn
            if self._turn == 1:
                self._turn = 2
            else:
                self._turn = 1
            return True

        if difference == False:
            return False
            
        if 1 in self._board.get(move_coord) or 2 in self._board.get(move_coord):
            #if player tries to move to a square that already has a pawn,
            return False
        
        if self.is_horizontal_move(start_coord, move_coord):
            #if it's a horizontal move
            if 'v' in self._board.get(move_coord):
                #if there is a vertical fence
                return False
            else:
                self.set_location_pawn(pawn, move_coord)
                self.delete_current_location(pawn, start_coord)
                #update player turn
                if self._turn == 1:
                    self._turn = 2
                else:
                    self._turn = 1
                return True
        else:
            if 'h' in self._board.get(move_coord):
                #if there is a horizontal fence
                return False
            else:
                #set the new location and return True
                self.set_location_pawn(pawn, move_coord)
                self.delete_current_location(pawn, start_coord)
                #update player turn
                if self._turn == 1:
                    self._turn = 2
                else:
                    self._turn = 1
                return True

    def place_fence(self, pawn, direction_of_fence, coord_to_place_fence):
        """* `place_fence` method takes following parameters in order: an integer that represents which player (1 or 2) is making the move, a letter indicating whether it is vertical (v) or horizontal (h) fence, a tuple of integers that represents the position on which the fence is to be placed.   
            - if player has no fence left, or if the fence is out of the boundaries of the board, or if there is already a fence there and the new fence will overlap or intersect with the existing fence, return `False`. 
            - If the fence can be placed, return `True`.
            - If it breaks the fair-play rule (and if you are doing the extra credit part), return exactly the string `breaks the fair play rule`.
            - If the game has been already won, return `False`"""
        #check that no one has won by calling is_winner
        #needs to check if player has fences left and if yes, how many
        if pawn == 1:
            #if pawn is 1
            if self._pawn1fences <= 0:
                return False
        elif pawn == 2:
            if self._pawn2fences <= 0:
                return False
        #check it's the player's turn
        if self._turn != pawn:
            return False
        if self.is_winner(pawn):
            #if True,return False
            return False
        #if yes,
        if coord_to_place_fence[0] < 0 or coord_to_place_fence[0] > 8 or coord_to_place_fence[1] < 0 or coord_to_place_fence[1] > 8:
        #check that the fence coordinates are not out of bounds, if yes, return False
            return False
        if direction_of_fence == 'h':
            #if it's a horizontal fence
            if 'h' in self._board.get(coord_to_place_fence):
                #if there is already an 'h' fence there
                return False
        elif direction_of_fence == 'v':
            #if it's a vertical fence
            if 'v' in self._board.get(coord_to_place_fence):
                #if a 'v' fence is already there
                return False
        #else find the key that matches the coord_to_place_fence
        self.set_location_fence(direction_of_fence, coord_to_place_fence)
        if pawn == 1:
            self._pawn1fences = self._pawn1fences - 1
        if pawn == 2:
            self._pawn2fences = self._pawn2fences - 1
        if self._turn == 1:
            self._turn = 2
        else:
            self._turn = 1
        return True
    
    def is_winner(self, pawn):
        """* `is_winner` method that takes a single integer representing the player number as a parameter and returns `True` if that player has won and `False` if that player has not won."""
        #find the current location of pawn by calling current_location
        start_coords = self.current_location(pawn)
        if pawn == 1:
            if start_coords[1] == 8:
                #if pawn1 is on the y coordinate 8
                #pawn1 wins, return true
                return True
        if pawn == 2:
            if start_coords[1] == 0:
                #if pawn2 is on y coordinate 0
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

""" game = QuoridorGame()
game.print_board()
print("2, 3,1 results in: ", game.move_pawn(2, (3,1)))
game.print_board()
print("1, 4,1 results in: ", game.move_pawn(1, (4,1)))
game.print_board()
print("2, 4,7 results in: ", game.move_pawn(2, (4,7)))
game.print_board()
print("1 places 'v' fence: ", game.place_fence(1, 'v', (1,3)))
game.print_board()
print("pawn1 fences, ", game._pawn1fences) """
