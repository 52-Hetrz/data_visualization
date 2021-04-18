"""
@Project    ：data_visualization 
@File       ：scatter_squares.py
@Description：使用scatter绘制散点图
@Author     ：Life
@Date       ：2021/4/18 19:51 
"""
import matplotlib.pyplot as plt


input_values = [1, 1, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.scatter(input_values, squares, s=100)
plt.title("scatter square", fontsize=24)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.show()

"""自动计算y的值"""
x_values = list(range(1, 10001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=1, edgecolors="none", c="red")
plt.title("无边界轮廓")
plt.show()
plt.scatter(x_values, y_values, s=1, c="green")
plt.title("有边界轮廓")
plt.show()

# 设置渐变颜色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors="none", s=10)
plt.show()

"""使用savefig()函数将图像输出"""
x_values_cubic = list(range(1000))
y_values_cubic = [x**3 for x in x_values_cubic]
plt.scatter(x_values_cubic, y_values_cubic, c=y_values_cubic, cmap=plt.cm.Blues,
            edgecolors="none", s=10)
plt.savefig("scatter_cubic_cmap.png", bbox_inches='tight')

