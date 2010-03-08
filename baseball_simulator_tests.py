import unittest
from baseball_simulator import BaseballSimulator, TOP_OF_INNING, BOTTOM_OF_INNING

THREE_STRIKES = 3
THREE_OUTS = 3
INNING_HALVES = 2
INNINGS = 9

class TestBaseBallSimulator(unittest.TestCase):
    def setUp(self):
        self.baseball_simulator = BaseballSimulator()

    def test_strike(self):
        self.baseball_simulator.strike()
        self.assertEqual(self.baseball_simulator.get_num_strikes(), 1)

        self.assertEqual(self.baseball_simulator.get_num_outs(), 0)
        self.baseball_simulator.strike()
        self.baseball_simulator.strike()
        self.assertEqual(self.baseball_simulator.get_num_outs(), 1)

        self.assertEqual(self.baseball_simulator.get_num_strikes(), 0)

    def test_ball(self):
        self.assertEqual(self.baseball_simulator.get_num_balls(), 0)
        self.baseball_simulator.ball()
        self.assertEqual(self.baseball_simulator.get_num_balls(), 1)
        
        self.baseball_simulator.ball()
        self.baseball_simulator.ball()
        self.baseball_simulator.ball()

        self.assertEqual(self.baseball_simulator.get_num_balls(), 0)

    def test_foul(self):
        self.assertEqual(self.baseball_simulator.get_num_strikes(), 0)
        self.baseball_simulator.foul()
        self.assertEqual(self.baseball_simulator.get_num_strikes(), 1)
        self.baseball_simulator.foul()
        self.baseball_simulator.foul()
        self.assertEqual(self.baseball_simulator.get_num_strikes(), 2)

#     def test_hit(self):
#         self.baseball_simulator.hit()

    def test_inning(self):
        self.assertEqual(self.baseball_simulator.get_inning(), 1)
        self.assertEqual(self.baseball_simulator.get_inning_half(), TOP_OF_INNING)

        for i in range(THREE_STRIKES * THREE_OUTS):
            self.baseball_simulator.strike()

        self.assertEqual(self.baseball_simulator.get_inning(), 1)
        self.assertEqual(self.baseball_simulator.get_inning_half(), BOTTOM_OF_INNING)

        for i in range(THREE_STRIKES * THREE_OUTS):
            self.baseball_simulator.strike()

        self.assertEqual(self.baseball_simulator.get_inning(), 2)
        self.assertEqual(self.baseball_simulator.get_inning_half(), TOP_OF_INNING)

    def test_game_over(self):
        self.assertFalse(self.baseball_simulator.is_game_over())
        for i in range(THREE_STRIKES * THREE_OUTS * INNING_HALVES * INNINGS):
            self.baseball_simulator.strike()

        self.assertFalse(self.baseball_simulator.is_game_over())

        for i in range(4):
            self.baseball_simulator.batter_hit_by_pitch()

        for i in range(THREE_STRIKES * THREE_OUTS * INNING_HALVES):
            self.baseball_simulator.strike()

        self.assertTrue(self.baseball_simulator.is_game_over())
        
    def test_walk(self):
        self.baseball_simulator.batter_hit_by_pitch()

        self.assertTrue(self.baseball_simulator.is_man_on_first())

        self.baseball_simulator.batter_hit_by_pitch()

        self.assertTrue(self.baseball_simulator.is_man_on_first())
        self.assertTrue(self.baseball_simulator.is_man_on_second())

        self.baseball_simulator.batter_hit_by_pitch()

        self.assertTrue(self.baseball_simulator.is_man_on_first())
        self.assertTrue(self.baseball_simulator.is_man_on_second())
        self.assertTrue(self.baseball_simulator.is_man_on_third())

        self.baseball_simulator.batter_hit_by_pitch()
        self.assertEqual(self.baseball_simulator.visiting_team.get_score(), 1)


    def test_hit(self):
        self.baseball_simulator.hit(RunnersAdvanceOne())
        self.baseball_simulator.hit(RunnersAdvanceOne())


if __name__ == '__main__':
    unittest.main()
