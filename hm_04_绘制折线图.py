# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

# matplotlib 默认不支持中文字符，因为默认的英文字体无法显示汉字
# 在linux/mac下 通过下面命令
# fc-list 查看支持的字体
# fc-list :lang=zh 查看支持的中文（冒号前面有空格）
# 通过在搜索下输入字体，出来很多可用的字体，我们选择其中有一个汉字打开，输入其文本文件位置即可
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SIMKAI.TTF")
x = range(0, 120)
# x是所有的0-119的整数

y = [random.randint(20, 35) for i in range(120)]
# 得到一个[20，35]的一个任意数据,得120次（0-119）

# 设置图片的大小
plt.figure(figsize=(15, 8), dpi=60)
# 绘图
plt.plot(x, y)
# 可以在绘图后对绘制的图进行添加信息或更改

# 绘制网格并调整线的透明度
plt.grid(alpha=0.4)
# 调整x轴的刻度，{}中的数据是i的形式的数
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]


# 取步长，数字和字符串意义对应，数据的长度一样
# rotation是旋转的度数
# fontproperties是选择的字体格式，避免出现乱码
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)
# 在这个位置保存的话，后面的操作就无法再保存的图片上显示
plt.savefig("./t1.png")
# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位(C)", fontproperties=my_font)
plt.title("10点到12点每分种的气温变化", fontproperties=my_font)
# 展示图形
plt.show()
