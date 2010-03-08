import unittest
from baseball_simulator import BaseballSimulator

class TestBaseBallSimulator(unittest.TestCase):
    def setUp(self):
        self.baseball_simulator = BaseballSimulator()

    def test_men_on_base(self):
        self.assertFalse(self.baseball_simulator.is_man_on_first())
        self.baseball_simulator.set_man_on_first()
        self.assertTrue(self.baseball_simulator.is_man_on_first())

        self.assertFalse(self.baseball_simulator.is_man_on_second())
        self.baseball_simulator.set_man_on_second()
        self.assertTrue(self.baseball_simulator.is_man_on_second())

        self.assertFalse(self.baseball_simulator.is_man_on_third())
        self.baseball_simulator.set_man_on_third()
        self.assertTrue(self.baseball_simulator.is_man_on_third())

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
        for i in range(9):
            self.baseball_simulator.strike()

        self.assertEqual(self.baseball_simulator.get_inning(), 2)

    def test_game_over(self):
        self.assertFalse(self.baseball_simulator.is_game_over())
        for i in range(3 * 3 * 9):
            self.baseball_simulator.strike()

        self.assertTrue(self.baseball_simulator.is_game_over())
        
    def test_walk(self):
        self.baseball_simulator.batter_hit_by_pitch()

        self.assertTrue(self.baseball_simulator.is_man_on_first())

        self.baseball_simulator.batter_hit_by_pitch()

        self.assertTrue(self.baseball_simulator.is_man_on_first())
        self.assertTrue(self.baseball_simulator.is_man_on_second())


# need to create score
#     def test_teams(self):
#         self.assertEqual(self.baseball_simulator.team1.get_score(), 0)


if __name__ == '__main__':
    unittest.main()
