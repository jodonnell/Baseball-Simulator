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

    def test_balls(self):
        self.baseball_simulator.set_num_balls(3)
        self.assertEqual(self.baseball_simulator.get_num_balls(), 3)


if __name__ == '__main__':
    unittest.main()
