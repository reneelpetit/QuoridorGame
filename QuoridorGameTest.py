import unittest
from Quoridor import QuoridorGame

class TestQuoridor(unittest.TestCase):

    def test_a_game_object_can_be_created(self):
        q = QuoridorGame()
        self.assertIsInstance(q, QuoridorGame)

    def test_move_pawn_can_move_pawn_for_player1(self):
        q = QuoridorGame()
        self.assertTrue(q.move_pawn(1, (4,1)))
    
    def test_move_pawn_can_move_pawn_for_player2(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        self.assertTrue(q.move_pawn(2, (4,7)))
    
    def test_player1_is_winner_true(self):
        q = QuoridorGame()
        q.delete_current_location(1, (4,0))
        q.set_location_pawn(1, (4,8))
        self.assertTrue(q.is_winner(1))
    
    def test_player1_is_winner_false(self):
        q = QuoridorGame()
        self.assertFalse(q.is_winner(1))
    
    def test_player2_is_winner_true(self):
        q = QuoridorGame()
        q.delete_current_location(2, (4,8))
        q.set_location_pawn(2, (4,0))
        self.assertTrue(q.is_winner(2))
    
    def test_player2_is_winner_false(self):
        q = QuoridorGame()
        self.assertFalse(q.is_winner(2))
    
    def test_player1_cannot_leave_board(self):
        q = QuoridorGame()
        self.assertFalse(q.move_pawn(1, (4,-1)))
    
    def test_player2_cannot_leave_board(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        self.assertFalse(q.move_pawn(2, (4,9)))
    
    def test_diagnol_move_not_allowed_player1(self):
        q = QuoridorGame()
        self.assertFalse(q.move_pawn(1, (3,1)))
    
    def test_diagnol_move_not_allowed_player2(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        self.assertFalse(q.move_pawn(2, (3,7)))
    
    def test_more_than_1_space_move_not_allowed_player1(self):
        q = QuoridorGame()
        self.assertFalse(q.move_pawn(1, (4,3)))
    
    def more_than_1_space_move_not_allowed_player2(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        self.assertFalse(q.move_pawn(2, (4,4)))
    
    def check_horizontal_move_true(self):
        q = QuoridorGame()
        self.assertTrue(q.is_horizontal_move((3,2), (2,2)))
    
    def check_horizontal_move_false(self):
        q = QuoridorGame()
        self.assertFalse(q.is_horizontal_move((3,2), (4,3)))

if __name__ == '__main__':
    unittest.main()