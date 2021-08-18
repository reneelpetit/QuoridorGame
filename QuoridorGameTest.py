import unittest
import Quoridor

def test_a_game_object_can_be_created(self):
    q = Quoridor()
    self.assertInInstance(q, Quoridor)

def test_move_pawn_can_move_pawn_for_player1(self):
    q = Quoridor()
    q.move_pawn(1, (4,1))

if __name__ == '__main__':
    unittest.main()