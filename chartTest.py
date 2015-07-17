from matplotlib import cm
import matplotlib.pyplot as plt

#data
x=[1,2,4]
y=[11,12,8]

for i in range(0,len(x)):
  plt.bar(x[i],y[i],color=cm.jet(1.*i/len(x)))

plt.show()