import unittest
from baseball_simulator import BaseballSimulator, DoubleStrategy, SingleStrategy, OutStrategy, TOP_OF_INNING, BOTTOM_OF_INNING

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

        
        self.baseball_simulator.hit(DoubleStrategy())
        self.baseball_simulator.hit(DoubleStrategy())

        for i in range(THREE_STRIKES * THREE_OUTS * INNING_HALVES):
            self.baseball_simulator.strike()

        self.assertTrue(self.baseball_simulator.is_game_over())
        
    def test_hit(self):
        self.baseball_simulator.hit(DoubleStrategy())
        self.assertFalse(self.baseball_simulator.bases.first_base.is_runner_on())
        self.assertTrue(self.baseball_simulator.bases.second_base.is_runner_on())

        self.baseball_simulator.hit(SingleStrategy())
        self.assertTrue(self.baseball_simulator.bases.first_base.is_runner_on())
        self.assertFalse(self.baseball_simulator.bases.second_base.is_runner_on())
        self.assertTrue(self.baseball_simulator.bases.third_base.is_runner_on())

        self.baseball_simulator.hit(SingleStrategy())
        self.assertEqual(self.baseball_simulator.visiting_team.get_score(), 1)

        self.baseball_simulator.hit(OutStrategy())
        self.assertEqual(self.baseball_simulator.get_num_outs(), 0)
        self.assertEqual(self.baseball_simulator.get_inning_half(), BOTTOM_OF_INNING)


if __name__ == '__main__':
    unittest.main()
