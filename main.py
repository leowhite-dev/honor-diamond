import matplotlib.pyplot as plt
import numpy as np
"""
每个图像均包含2条曲线，分别是原始概率和3倍概率的曲线。

图像1:
    假设每次抽奖的概率为0.008

图像2:
    每次抽奖的概率从0到0.016按次数直线增加。
"""

def graph1():
    plt.figure(figsize=(10, 7.5))   #根据我自己的显示器设置的尺寸
    
    # Line 1: Original PROBABILITY = 0.008
    OrigPROBABILITY = 0.008
    chance1 = []
    for i in range(1,361):
        chance1.append(1 - (1-OrigPROBABILITY)**i)
    plt.plot(range(1, 361), chance1, label='p=0.008')
    
    # Line 2: 3timesPROBABILITY = Original PROBABILITY * 3
    ThreeTimesPROBABILITY = OrigPROBABILITY * 3
    chance2 = []
    for i in range(1,301):
        chance2.append(1 - (1-ThreeTimesPROBABILITY)**i)
    plt.plot(range(1, 301), chance2, label='p=0.024')
    
    plt.xlabel('Index')
    plt.ylabel('Chance')
    plt.title('Probability Curves')
    plt.grid(True)
    plt.yticks(np.arange(0, 1.01, 0.05))
    plt.xlim(0, 361)
    plt.legend()
    plt.show()

def graph2():
    # Line 1: Original PROBABILITY increases linearly from 0 to 0.016
    OrigPOSSIBILITIES = [ (i - 1) * 0.016 / 360 for i in range(1, 361)]
    chance1 = []
    for i in range(1,361):
        chance1.append(1 - (1-OrigPOSSIBILITIES[i-1])**i)
    plt.plot(range(1, 361), chance1, label='p increases linearly from 0 to 0.016')

    # Line 2: 3timesPROBABILITY = Original PROBABILITY * 3
    ThreeTimesPOSSIBILITIES = [ min(p * 3, 1) for p in OrigPOSSIBILITIES]
    chance2 = []
    for i in range(1,361):
        chance2.append(1 - (1-ThreeTimesPOSSIBILITIES[i-1])**i)
    plt.plot(range(1, 361), chance2, label='p increases linearly from 0 to 0.048')
    plt.xlabel('Index')
    plt.ylabel('Chance')
    plt.title('Probability Curves with Linearly Increasing Probability')
    plt.grid(True)
    plt.yticks(np.arange(0, 1.01, 0.05))
    plt.xlim(0, 301)
    plt.legend()
    plt.show()

    
if __name__ == "__main__":
    graph1()
    graph2()