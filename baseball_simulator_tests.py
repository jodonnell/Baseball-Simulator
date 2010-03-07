import unittest
from baseball_simulator import BaseballSimulator

class TestBaseBallSimulator(unittest.TestCase):
    def setUp(self):
        self.baseball_simulator = BaseballSimulator()

    def test_men_on_base(self):
        self.assertFalse(self.baseball_simulator.is_man_on_first())
        self.baseball_simulator.put_man_on_first()
        self.assertTrue(self.baseball_simulator.is_man_on_first())



if __name__ == '__main__':
    unittest.main()
