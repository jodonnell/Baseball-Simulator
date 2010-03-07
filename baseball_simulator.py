
class BaseballSimulator(object):
    def __init__(self):
        self.men_on_base = []

    def put_man_on_first(self):
        if 1 not in self.men_on_base:
            self.men_on_base.append(1)

    def is_man_on_first(self):
        if 1 in self.men_on_base:
            return True

        return False

