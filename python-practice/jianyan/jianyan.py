# -*- coding: utf-8 -*
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['axes.unicode_minus']=False
#当负号无法正常显示时添加上面这行代码

plt.rcParams['font.sans-serif'] = ['SimHei']
#对中文进行支持
plt.title('线图示例')
#设置图片的题注

x = np.linspace(-1,10,20)
#在-1到10的区间内生成20个数据
y1 = 100*x + 10
#直线y1
y2 = 2**x
#曲线y2

plt.plot(x,y1,'r+',color = 'b',linewidth = 1.0,linestyle = '-',label = 'line1')
plt.plot(x,y2,'bo',color = '#800080',linewidth = 2.0,linestyle = '--',label = 'line2')
plt.xlim(-2,11)
#设置横轴的最大值与最小值
plt.legend(['y=100x+10','y=2^x'],loc = 'upper left')

plt.show()