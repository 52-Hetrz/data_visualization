"""
@Project    ：data_visualization 
@File       ：mpl_squares.py
@Description：绘制简单的折线图
@Author     ：Life
@Date       ：2021/4/18 14:43 
"""
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
print(squares[-1])
# 同时传入横纵坐标
plt.plot(input_values, squares, linewidth=3)

# 设置图像的标签和横纵坐标
plt.title("square of numbers", fontsize=24)
plt.xlabel("x", fontsize=14)
plt.ylabel("square", fontsize=14)

# 设置刻度大小
plt.tick_params(axis="both", labelsize=14)
plt.show()
