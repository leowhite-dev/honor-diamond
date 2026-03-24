import matplotlib.pyplot as plt
import numpy as np

# 设置matplotlib中文字体
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
"""
每个图像均包含2条曲线，分别是原始概率和3倍概率的曲线。

图像1:
    每次抽奖的概率从0到0.016按次数直线增加。
"""
def Graph_line():
    plt.figure(figsize=(10, 7.5))   # New figure for graph2
    # Line 1: Original PROBABILITY increases linearly from 0 to 0.016
    OrigPOSSIBILITIES = [ (i - 1) * 0.016 / 360 for i in range(1, 361)]
    chance_line = []
    for i in range(1,361):
        chance_line.append(1 - (1-OrigPOSSIBILITIES[i-1])**i)
    chance_line.append(1)
    plt.plot(range(1, 362), chance_line, label='中奖概率从0到0.016线性增加')

    # Line 2: 3timesPROBABILITY = Original PROBABILITY * 3
    ThreeTimesPOSSIBILITIES = [ min(p * 3, 1) for p in OrigPOSSIBILITIES]
    chance2 = []
    for i in range(1,301):
        chance2.append(1 - (1-ThreeTimesPOSSIBILITIES[i-1])**i)
    plt.plot(range(1, 301), chance2, label='3倍概率', linestyle='--')
    plt.xlabel('Index')
    plt.ylabel('Chance')
    plt.title('Probability Curves with Linearly Increasing Probability')
    plt.grid(True)
    plt.yticks(np.arange(0, 1.01, 0.05))
    plt.xlim(0, 361)
    plt.legend()
    plt.savefig('./Graph/Graph_line.png')
    # plt.show()

    
if __name__ == "__main__":
    Graph_line()