import unittest
from Quoridor import QuoridorGame

class TestQuoridor(unittest.TestCase):

    def test_a_game_object_can_be_created(self):
        q = QuoridorGame()
        self.assertIsInstance(q, QuoridorGame)

    def test_move_pawn_can_move_pawn_for_player1(self):
        q = QuoridorGame()
        self.assertTrue(q.move_pawn(1, (4,1)))

if __name__ == '__main__':
    unittest.main()