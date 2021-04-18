"""
@Project    ：data_visualization 
@File       ：random_walk.py
@Description：随机漫步
@Author     ：Life
@Date       ：2021/4/18 20:11 
"""

from random import choice
import matplotlib.pyplot as plt


def get_distance_direction():
    x_direction = choice([-1, 1])
    x_distance = choice([1, 2, 3, 4, 5])
    return x_distance, x_direction


class RandomWalk:
    def __init__(self, initial_x, initial_y, max_steps):
        self.x = [initial_x]
        self.y = [initial_y]
        self.max_steps = max_steps

    def walk_one_step(self):
        """走一步"""
        x_distance, x_direction = get_distance_direction()
        x_step = self.x[-1]+x_distance * x_direction
        y_distance, y_direction = get_distance_direction()
        y_step = self.y[-1] + y_distance * y_direction
        self.x.append(x_step)
        self.y.append(y_step)

    def walk(self):
        """随机漫步"""
        while len(self.x) < self.max_steps:
            self.walk_one_step()


random_walk = RandomWalk(0, 0, 50000)
random_walk.walk()
steps = random_walk.max_steps
colors = list(range(steps))
plt.scatter(random_walk.x, random_walk.y, edgecolors="none",
            s=2, c=colors, cmap=plt.cm.Blues)
# 设置初始点和结束点的大小
plt.scatter(0, 0, c="red", s=20, edgecolors="none")
plt.scatter(random_walk.x[-1], random_walk.y[-1], c="black", s=20)
plt.title("Random Walk", fontsize=24, c="black")
# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.figure(figsize=(20, 12))
plt.show()
