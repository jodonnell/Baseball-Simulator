
FIRST_BASE = 1
SECOND_BASE = 2
THIRD_BASE = 3

class BaseballSimulator(object):
    def __init__(self):
        self._men_on_base = []
        self._num_balls = 0

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
        self._num_balls = num_balls

    def get_num_balls(self):
        return self._num_balls
