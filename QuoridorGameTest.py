import unittest
import QuoridorGame

def test_a_game_object_can_be_created(self):
    q = QuoridorGame()
    self.assertInInstance(q, QuoridorGame)

def test_move_pawn_can_move_pawn_for_player1(self):
    q = QuoridorGame()
    q.move_pawn(1, (4,1))

if __name__ == '__main__':
    unittest.main()