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
    
    def test_more_than_1_space_move_not_allowed_player2(self):
        q = QuoridorGame()
        q.move_pawn(1, (4,1))
        self.assertFalse(q.move_pawn(2, (4,4)))
    
    def test_check_horizontal_move_true(self):
        q = QuoridorGame()
        self.assertTrue(q.is_horizontal_move((3,2), (2,2)))
    
    def test_check_horizontal_move_false(self):
        q = QuoridorGame()
        self.assertFalse(q.is_horizontal_move((3,2), (4,3)))
    
    def test_check_player1_fences_decrease(self):
        q = QuoridorGame()
        q.place_fence(1, 'v', (3,3))
        self.assertEqual(q._pawn1fences, 9)
    
    def test_check_player2_fences_decrease(self):
        q = QuoridorGame()
        q.place_fence(1, 'v', (2,1))
        q.place_fence(2, 'h', (3,3))
        self.assertEqual(q._pawn2fences, 9)
    
    def test_check_player1_can_place_fence_true(self):
        q = QuoridorGame()
        q.place_fence(1, 'v', (1,3))
        for key, value in q._board.items():
            if key == (1,3):
                if 'v' in value:
                    key = True
        self.assertTrue(key)
    
    def test_check_player2_can_place_fence_true(self):
        q = QuoridorGame()
        q.place_fence(2, 'h', (1,3))
        for key, value in q._board.items():
            if key == (1,3):
                if 'h' in value:
                    key = True
        self.assertTrue(key) 

    def test_check_player1_cannot_place_fence_over_fence(self):  
        q = QuoridorGame()
        q.place_fence(1, 'h', (5,2))
        self.assertFalse(q.place_fence(1, 'h', (5,2)))
    
    def test_check_player2_cannot_place_fence_over_fence(self):
        q = QuoridorGame()
        q.place_fence(1, 'v', (5,2))
        self.assertFalse(q.place_fence(2, 'v', (5,2)))
    
    def test_check_player_cannot_move_out_of_turn_fence(self):
        q = QuoridorGame()
        self.assertFalse(q.place_fence(2, 'h', (5,5)))
    
    def test_check_player_cannot_move_out_of_turn(self):
        q = QuoridorGame()
        self.assertFalse(q.move_pawn(2, (3,8)))
    
    def test_check_diagnol_move_is_allowed_up_right(self):
        q = QuoridorGame()
        q.delete_current_location(1, (4,0))
        q.delete_current_location(2, (4,8))
        q.set_location_fence('h', (1,1))
        q.set_location_pawn(1, (1,2))
        q.set_location_pawn(2, (1,3))
        q._turn = 2
        self.assertTrue(q.is_diagonal_allowed(2, (1,3), (2,2)))

    def test_check_diagnol_move_is_allowed_down_right(self):
        q = QuoridorGame()
        q.delete_current_location(1, (4,0))
        q.delete_current_location(2, (4,8))
        q.set_location_fence('h', (1,3))
        q.set_location_pawn(1, (1,2))
        q.set_location_pawn(2, (1,3))
        q._turn = 1
        self.assertTrue(q.is_diagonal_allowed(1, (1,2), (2,3)))

    def test_check_diagnol_move_is_allowed_down_left(self):
        q = QuoridorGame()
        q.delete_current_location(1, (4,0))
        q.delete_current_location(2, (4,8))
        q.set_location_fence('h', (1,3))
        q.set_location_pawn(1, (1,2))
        q.set_location_pawn(2, (1,3))
        q._turn = 1
        self.assertTrue(q.is_diagonal_allowed(1, (1,2), (0,3)))

    def test_check_diagnol_move_is_allowed_up_left(self):
        q = QuoridorGame()
        q.delete_current_location(1, (4,0))
        q.delete_current_location(2, (4,8))
        q.set_location_fence('h', (1,1))
        q.set_location_pawn(1, (1,2))
        q.set_location_pawn(2, (1,3))
        q._turn = 2
        self.assertTrue(q.is_diagonal_allowed(2, (1,3), (0,2)))
    
    def test_check_diagnol_move_with_zero(self):
        q = QuoridorGame()
        q.delete_current_location(1, (4,0))
        q.delete_current_location(2, (4,8))
        q.set_location_fence('h', (0,0))
        q.set_location_pawn(1, (0,1))
        q.set_location_pawn(2, (0,2))
        q._turn = 2
        self.assertTrue(q.is_diagonal_allowed(2, (0,2), (1,1)))

    def test_check_jump_over_condition_allowed_player1(self):
        q = QuoridorGame()
        q.delete_current_location(1, (4,0))
        q.delete_current_location(2, (4,8))
        q.set_location_pawn(1, (3,4))
        q.set_location_pawn(2, (3,5))
        q._turn = 1
        self.assertTrue(q.check_jump_over_valid(1, (3,4), (3,6)))
    
    def test_check_jump_over_condition_allowed_player2(self):
        q = QuoridorGame()
        q.delete_current_location(1, (4,0))
        q.delete_current_location(2, (4,8))
        q.set_location_pawn(1, (3,4))
        q.set_location_pawn(2, (3,5))
        q._turn = 2
        self.assertTrue(q.check_jump_over_valid(2, (3,5), (3,3)))

    def test_check_jump_over_condition_not_allowed_fence_player1(self):
        pass

    def test_check_jump_over_condition_not_allowed_fence_player2(self):
        pass

if __name__ == '__main__':
    unittest.main()