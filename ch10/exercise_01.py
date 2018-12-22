import pylab as pl
import matplotlib.pyplot as plt
import math


'''
绘制sin函数曲线
'''


def learn_sin():
    print("sin(3) : %.4f" % math.sin(3))
    print("sin(-3) : %.4f" % math.sin(-3))
    print("sin(0) %.4f: " % math.sin(0))
    print("sin(math.pi) : %.4f" % math.sin(math.pi))
    print("sin(math.pi/2) : %.4f" % math.sin(math.pi/2))

    degree = 90
    rad = degree*math.pi/180
    print("sin(90degree) : %f" % math.sin(rad))


def draw_sin():
    data_len = 100
    x = [0] * data_len
    y = [0] * data_len
    for i in range(data_len):
        v = i/10
        x[i] = v
        # 纵轴的数据
        y[i] = math.sin(v)

    # 高级用法
    #y = [math.sin(i) for i in x]

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label="$sin(x)$",color="red",linewidth=2)
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("PyPlot First Example")
    plt.legend()  # 显示左下角的图例
    #plt.savefig(r"save_test.png", dpi=600)  # 默认像素dpi是80
    plt.grid()  # 生成网格
    plt.show()

if __name__ == "__main__":
    #learn_sin()
    draw_sin()