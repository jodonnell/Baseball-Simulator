
FIRST_BASE = 1
SECOND_BASE = 2
THIRD_BASE = 3

class BaseballSimulatorExceptions(Exception):
    pass

class Team(object):
    def __init__(self):
        self._score = 0

    def get_score(self):
        return self._score

    def score(self):
        self._score += 1

class BaseballSimulator(object):
    def __init__(self):
        self._men_on_base = []
        self._num_balls = 0
        self._num_strikes = 0
        self._num_outs = 0
        self._inning = 1
        self._game_over = False
        self.team1 = Team()
        self.team2 = Team()

    def _set_man_on(self, base):
        if base not in self._men_on_base:
            self._men_on_base.append(base)

    def _is_man_on_base(self, base):
        if base in self._men_on_base:
            return True
        return False

    def set_man_on_first(self):
        self._set_man_on(FIRST_BASE)

    def set_man_on_second(self):
        self._set_man_on(SECOND_BASE)

    def set_man_on_third(self):
        self._set_man_on(THIRD_BASE)

    def is_man_on_first(self):
        return self._is_man_on_base(FIRST_BASE)

    def is_man_on_second(self):
        return self._is_man_on_base(SECOND_BASE)

    def is_man_on_third(self):
        return self._is_man_on_base(THIRD_BASE)

    def get_num_balls(self):
        return self._num_balls

    def get_num_strikes(self):
        return self._num_strikes

    def get_num_outs(self):
        return self._num_outs

    def is_game_over(self):
        return self._game_over

    def strike(self):
        self._num_strikes += 1
        if self._num_strikes == 3:
            self._out()
            self._new_at_bat()

    def ball(self):
        self._num_balls += 1
        if self._num_balls == 4:
            self._walk()
            self._new_at_bat()

    def _walk(self):
        self.set_man_on_first()

    def foul(self):
        if self._num_strikes < 2:
            self._num_strikes += 1

    # multiple things can happen, any runner can be out
    def hit(self, hit_strategy):
#        hit_strategy.
        pass

    def _out(self):
         self._num_outs += 1
         if self._num_outs == 3:
             self._num_outs = 0
             self._new_at_bat()
             self._new_inning()

    def _new_inning(self):
        self._inning += 1
        if self._inning == 9:
            self._game_over = True

    def get_inning(self):
        return self._inning

    def _new_at_bat(self):
        self._num_strikes = 0
        self._num_balls = 0

# output game state after play, strikes could be up, balls, outs, reset balls and strikes on end of bat

# ['Base hit', 'Double', 'Triple', 'Home run', 'Strike', 'Foul', 'Ball', 'Walk (batter hit)', 'Popup',
# 'Strike Out', 'Walk (4 balls)', 'X runs scored', 'Inning over', 'Grand Slam', 'Runner advances from x to x', 'Runner x is out'

# ]

if __name__ == '__main__':
    baseball_simulator = BaseballSimulator()
    baseball_simulator.set_num_strikes(2)
    baseball_simulator.set_num_outs(2)
    print baseball_simulator.get_possible_plays()
    
