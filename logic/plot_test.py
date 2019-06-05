#python -m pip install numpy
#python -m pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt
 
# ランダムに点をプロット
x = np.random.randint(1,5,5)
y = np.random.randint(1,5,5)
 
# matplotlibの描画オブジェクト#1を作成
ax1 = plt.subplot(1,2,1)
# 散布図を作成
ax1.scatter(x,y)
ax1.axis([0,10,0,10])
ax1.grid(True)
 
# 極座標に変換
radii = np.sqrt(x**2 + y**2)
theta = np.arctan2(y,x)
 
# matplotlibの描画オブジェクト#2を作成
ax2 = plt.subplot(1,2,2,polar=True)
# 散布図を作成
ax2.scatter(theta,radii)
ax2.set_rmax(10)
ax2.grid(True)
 
# 表示を実行
plt.show()
