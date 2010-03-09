"""
A program that simulates a baseball game.

Unfortunately, I did not have the time to fully flesh it out (baseball's complicated!).
Some missing functionality includes, for a strategy where a runner could run past another 
runner which is not allowed in baseball.
Also the logic for driving a hit got kind of ugly, ie having set_runner_on overloaded to cause an out.
"""

import random

FIRST_BASE = 1
SECOND_BASE = 2
THIRD_BASE = 3

TOP_OF_INNING = 1
BOTTOM_OF_INNING = 2

BALLS_TO_WALK = 4
INNINGS_IN_GAME = 9

STRIKES_IN_OUT = 3

OUTS_IN_AT_BAT = 3


# Strategies that implement what happens when a hit is made.
class SingleStrategy(object):
    def decide(self, current_base):
        return current_base.get_next_base()

class DoubleStrategy(object):
    def decide(self, current_base):
        next_base = current_base.get_next_base()
        return next_base.get_next_base()

class OutStrategy(object):
    def decide(self, current_base):
        return Out()

class RandomStrategy(object):
    def decide(self, current_base):
        if random.randint(0, 1):
            return current_base.get_next_base()
        return Out()


# Classes that represent bases and possible play outcomes
class BaseAbstract(object):
    def __init__(self, next_base=None):
        self._next_base = next_base

    def get_next_base(self):
        return self._next_base

    def is_runner_on(self):
        return self._is_man_on

    def set_runner_on(self, runner_on, team_at_bat, baseball_simulator):
        "This should really use the command pattern rather than passing all possibly needed vars"
        pass

class Base(BaseAbstract):
    def __init__(self, next_base):
        super(Base, self).__init__(next_base)
        self._is_man_on = False

    def set_runner_on(self, runner_on, team_at_bat, baseball_simulator):
        self._is_man_on = runner_on

class HomeBase(BaseAbstract):
    def set_runner_on(self, runner_on, team_at_bat, baseball_simulator):
        team_at_bat.score()

class Out(BaseAbstract):
    def set_runner_on(self, runner_on, team_at_bat, baseball_simulator):
        baseball_simulator.out()

class Hitter(BaseAbstract):
    def __init__(self, next_base):
        super(Hitter, self).__init__(next_base)
        self._is_man_on = True

    def set_runner_on(self, runner_on, team_at_bat, baseball_simulator):
        self._is_man_on = True # score

class Bases(object):
    def __init__(self):
        self.home_base = HomeBase()
        self.third_base = Base(self.home_base)
        self.second_base = Base(self.third_base)
        self.first_base = Base(self.second_base)
        self.hitter = Hitter(self.first_base)

    def advance_runners(self, hit_strategy, team_at_bat, baseball_simulator):
        for base in (self.third_base, self.second_base, self.first_base, self.hitter):
            if base.is_runner_on():
                base.set_runner_on(False, team_at_bat, baseball_simulator)
                new_position = hit_strategy.decide(base) # will either place runner on base or remove him completely from play
                new_position.set_runner_on(True, team_at_bat, baseball_simulator)

class Inning(object):
    def __init__(self, visiting_team):
        self._inning = 1
        self._inning_half = TOP_OF_INNING
        self._team_at_bat = visiting_team

    def get_inning_half(self):
        return self._inning_half

    def get_inning(self):
        return self._inning

    def at_bat_over(self, home_team, visiting_team):
        if self._inning_half == TOP_OF_INNING:
            self._inning_half = BOTTOM_OF_INNING
            self._team_at_bat = home_team
        elif self._inning_half == BOTTOM_OF_INNING:
            self._inning_half = TOP_OF_INNING
            self._inning += 1
            self._team_at_bat = visiting_team

    def could_game_be_over(self):
        return self._inning > INNINGS_IN_GAME and self._inning_half == TOP_OF_INNING

    def get_team_at_bat(self):
        return self._team_at_bat

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
        self._game_over = False
        self.visiting_team = Team()
        self.home_team = Team()
        self._inning = Inning(self.visiting_team)
        self.bases = Bases()

    def get_num_balls(self):
        return self._num_balls

    def get_num_strikes(self):
        return self._num_strikes

    def get_num_outs(self):
        return self._num_outs

    def is_game_over(self):
        return self._game_over

    def is_score_tied(self):
        if self.home_team.get_score() == self.visiting_team.get_score():
            return True
        return False

    def get_inning(self):
        return self._inning.get_inning()

    def get_inning_half(self):
        return self._inning.get_inning_half()

    def strike(self):
        self._num_strikes += 1
        if self._num_strikes == STRIKES_IN_OUT:
            self.out()
            self._new_at_bat()

    def ball(self):
        "Unfinished"
        self._num_balls += 1
        if self._num_balls == BALLS_TO_WALK:
            #self._walk()
            self._new_at_bat()

    def foul(self):
        if self._num_strikes < STRIKES_IN_OUT - 1:
            self._num_strikes += 1

    def hit(self, hit_strategy):
        self.bases.advance_runners(hit_strategy, self._inning.get_team_at_bat(), self)

    def out(self):
         self._num_outs += 1
         if self._num_outs == OUTS_IN_AT_BAT:
             self._num_outs = 0
             self._change_team_at_bat()

    def _change_team_at_bat(self):
        self._new_at_bat()
        self._inning.at_bat_over(self.home_team, self.visiting_team)

        if self._inning.could_game_be_over() and not self.is_score_tied():
            self._game_over = True

    def _new_at_bat(self):
        self._num_strikes = 0
        self._num_balls = 0

if __name__ == '__main__':
    baseball_simulator = BaseballSimulator()
    while not baseball_simulator.is_game_over():
        baseball_simulator.hit(RandomStrategy())

    print "Visting team: %i" % baseball_simulator.visiting_team.get_score()
    print "Home team: %i" % baseball_simulator.home_team.get_score()
