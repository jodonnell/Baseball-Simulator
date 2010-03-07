
FIRST_BASE = 1
SECOND_BASE = 2
THIRD_BASE = 3

class BaseballSimulatorExceptions(Exception):
    pass

class TooManyStrikes(BaseballSimulatorExceptions):
    pass

class TooManyBalls(BaseballSimulatorExceptions):
    pass

class TooManyOuts(BaseballSimulatorExceptions):
    pass

class BaseballSimulator(object):
    def __init__(self):
        self._men_on_base = []
        self._num_balls = 0
        self._num_strikes = 0
        self._num_outs = 0

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

    def set_num_balls(self, num_balls):
        if num_balls > 3:
            raise TooManyBalls()
        self._num_balls = num_balls

    def get_num_balls(self):
        return self._num_balls

    def set_num_strikes(self, num_strikes):
        if num_strikes > 2:
            raise TooManyStrikes()
        self._num_strikes = num_strikes

    def get_num_strikes(self):
        return self._num_strikes

    def set_num_outs(self, num_outs):
        if num_outs > 2:
            raise TooManyOuts()
        self._num_outs = num_outs
        
    def get_num_outs(self):
        return self._num_outs
