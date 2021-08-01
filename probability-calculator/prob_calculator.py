import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k in kwargs.keys():
            new = [str(k) for i in range(kwargs[k])]
            self.contents += new

    def draw(self, n):
        if n <= len(self.contents):
            drawn = [self.contents.pop(random.randint(0, len(self.contents) - 1)) for i in range(n)]
            drawn.sort()
            return drawn
        else:
            drawn = self.contents
            self.contents = []
            drawn.sort()
            return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    for i in range(num_experiments):
        x_hat = copy.deepcopy(hat)
        drawn = x_hat.draw(num_balls_drawn)
        drawn_dict = dict.fromkeys(drawn, 0)
        for i in drawn:
            drawn_dict[i] += 1
        a = [int(expected_balls[k]) <= int(drawn_dict.get(k, 0)) for k in expected_balls.keys()]
        if not False in a:
            counter += 1
    probability = counter / num_experiments
    return probability


