
FIRST_BASE = 1
SECOND_BASE = 2
THIRD_BASE = 3

TOP_OF_INNING = 1
BOTTOM_OF_INNING = 2

BALLS_TO_WALK = 4
INNINGS_IN_GAME = 9

class BaseballSimulatorExceptions(Exception):
    pass

class Inning(object):
    def __init__(self, visiting_team, home_team):
        self._inning = 1
        self._inning_half = TOP_OF_INNING
        self._visiting_team = visiting_team
        self._home_team = home_team
        self._team_at_bat = self._visiting_team

    def get_inning_half(self):
        return self._inning_half

    def get_inning(self):
        return self._inning

    def at_bat_over(self):
        if self._inning_half == TOP_OF_INNING:
            self._inning_half = BOTTOM_OF_INNING
            self._team_at_bat = self._home_team
        elif self._inning_half == BOTTOM_OF_INNING:
            self._inning_half = TOP_OF_INNING
            self._inning += 1
            self._team_at_bat = self._visiting_team

    def could_game_be_over(self):
        if self._inning > INNINGS_IN_GAME and self._inning_half == TOP_OF_INNING:
            return True
        return False

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
        self._inning = Inning(self.visiting_team, self.home_team)

    def _set_man_on(self, base):
        if base not in self._men_on_base:
            self._men_on_base.append(base)

    def _is_man_on_base(self, base):
        if base in self._men_on_base:
            return True
        return False

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
        if self._num_balls == BALLS_TO_WALK:
            self._walk()
            self._new_at_bat()

    def batter_hit_by_pitch(self):
        self._new_at_bat()
        self._walk()

    def _walk(self):
        if self.is_man_on_first() and self.is_man_on_second() and self.is_man_on_third():
            self._inning.get_team_at_bat().score()
        elif self.is_man_on_first() and self.is_man_on_second():
            self._set_man_on(THIRD_BASE)
        elif self.is_man_on_first():
            self._set_man_on(SECOND_BASE)

        self._set_man_on(FIRST_BASE)
        self._new_at_bat()

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
             self._change_team_at_bat()

    def _change_team_at_bat(self):
        self._inning.at_bat_over()
        if self._inning.could_game_be_over() and not self.is_score_tied():
            self._game_over = True

    def is_score_tied(self):
        if self.home_team.get_score() == self.visiting_team.get_score():
            return True
        return False

    def get_inning(self):
        return self._inning.get_inning()

    def get_inning_half(self):
        return self._inning.get_inning_half()

    def _new_at_bat(self):
        self._num_strikes = 0
        self._num_balls = 0

if __name__ == '__main__':
    baseball_simulator = BaseballSimulator()
