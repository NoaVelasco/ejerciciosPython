import random


class Hat:

    def __init__(self, **kwargs):
        self.contents_init = []
        for k, v in kwargs.items():
            for n in range(v):
                self.contents_init.append(k)

    def draw(self, number):

        self.contents = self.contents_init.copy()
        if number >= len(self.contents):
            return self.contents
        else:
            chosen_list = []
            for n in range(number):
                chosen_ball = random.choice(self.contents)
                chosen_list.append(chosen_ball)
                self.contents.remove(chosen_ball)
        return chosen_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    success_num = 0
    for n in range(num_experiments):

        draw_list = hat.draw(num_balls_drawn)
        condition_list = []
        for k, v in expected_balls.items():
            if k in draw_list:
                if v <= draw_list.count(k):
                    condition_list.append(True)
                else:
                    condition_list.append(False)
            else:
                condition_list.append(False)

        if False not in condition_list:
            success_num += 1

    return success_num / num_experiments


# hat_final = Hat(black=6, red=4, green=3)
# probability = experiment(hat=hat_final,
#                          expected_balls={"red": 2, "green": 1},
#                          num_balls_drawn=5,
#                          num_experiments=2000)

# random.seed(95)
# hat = Hat(blue=4, red=2, green=6)
# probability = experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=3000)
# print("Probability:", probability)

# print(probability)

hat = Hat(blue=3, red=2, green=6)
probability = experiment(hat=hat, expected_balls={
                         "blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
print(probability)
# expected = 0.272
# self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')

hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
probability = experiment(hat=hat, expected_balls={
                         "yellow": 2, "blue": 3, "test": 1}, num_balls_drawn=20, num_experiments=100)
print(probability)
# expected = 1.0
# self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')
