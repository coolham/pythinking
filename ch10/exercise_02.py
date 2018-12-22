import pylab as pl
import matplotlib.pyplot as plt
import math


'''
绘制sin函数曲线
'''


def draw_sin2():
    data_len = 360
    x = [0] * data_len
    y1 = [0] * data_len
    y2 = [0] * data_len
    for i in range(data_len):
        #转换成弧度
        r = i * math.pi / 180
        x[i] = i
        # 纵轴的数据
        y1[i] = math.sin(r)
        y2[i] = math.cos(r)
    # 高级用法
    #y = [math.sin(i) for i in x]

    plt.figure(figsize=(8, 4))
    plt.plot(x, y1, label="$sin(x)$",color="red",linewidth=2)
    plt.plot(x, y2, label="$cos(x)$",color="blue",linewidth=2)
    plt.xlabel(r"Degree")
    plt.title(r"角度的Sin值")
    plt.legend()  # 显示左下角的图例
    #plt.savefig(r"save_test.png", dpi=600)  # 默认像素dpi是80
    plt.grid()  # 生成网格
    plt.show()

if __name__ == "__main__":

    draw_sin2()