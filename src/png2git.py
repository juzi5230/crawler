# -*- encoding: utf-8 -*-
'''
@File    :   month_gif.py
@Time    :   2022/05/13 15:24:47
@Author  :   HMX 
@Version :   1.0
@Contact :   kzdhb8023@163.com
'''

# here put the import lib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1,figsize = (8,8))
fig.set_facecolor((0, 0, 0, 0.1))
imglist = []

for i in range(0,39):
    ax.set_axis_off()
    index = str(i)
    if i < 10: 
        index = str(0) + '' + str(i)
    im = ax.imshow(plt.imread(r'/Users/cheng/Desktop/crawler/loading/loading_000{}.png'.format(index)), animated = True)
    imglist.append([im])

ani = animation.ArtistAnimation(fig, imglist, interval=16)#interval时间间隔 单位毫秒
ani.save(r'/Users/cheng/Desktop/crawler/loading/2month.gif',dpi = 800)
plt.show()
print('ok')
