import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from pylab import *
from matplotlib import *

oldMeans = [0,1,4,8,8,8]
newMeans = [2,3,6,7,8,6]
change= []

#oldStd     = (2, 3, 4, 1, 2, 1)
#newStd   = (3, 5, 2, 3, 3, 2)
ind = np.arange(len(oldMeans))    # the x locations for the groups
width = .55       # the width of the bars: can also be len(x) sequence

plt.figure(1)
plt.subplot(121)
p1 = plt.barh(ind, oldMeans, width, color='b')#, bottom=(0,0,0,0,0,0)) #yerr=newStd
p2 = plt.barh(ind+.25, newMeans, width, color='y')#, bottom=(0,0,0,0,0,0)) #yerr=oldStd

plt.xlabel('No. of identified proteins')
plt.title('Identified proteins by fmol')
#plt.yticks(ind+width/2., ('0.5 fmol', '5 fmol', '50 fmol', '500 fmol', '5,000 fmol', '50,000 fmol') )
plt.xticks(np.arange(0,10,1))
plt.legend( (p1[0], p2[0]), ('Previous Study', 'This Study'), 4 )

for i in range(len(oldMeans)):
    try:
        change.append((newMeans[i] / oldMeans[i] - 1) * 100)
    except:
        change.append(100.0)

#############################################################################################

p3 = plt.subplot(122)

for i in range (-50,200):
    p3.barh(ind, change, width, color=cm.RdBu(i))#, color='c', bottom=(0,0,0,0,0,0)) #yerr=newStd
#p2 = plt.barh(ind+.25, newMeans, width, color='y')#, bottom=(0,0,0,0,0,0)) #yerr=oldStd

p3.set_xlabel('Percent change in No. of identified proteins')
p3.set_title('Percent change between studies')
#p3.set_yticks(ind+width/2., ('0.5 fmol', '5 fmol', '50 fmol', '500 fmol', '5,000 fmol', '50,000 fmol') )
yticks = ['0.5 fmol', '5 fmol', '50 fmol', '500 fmol', '5,000 fmol', '50,000 fmol']
p3.set_xticks(np.arange(-50,max(i for i in change),25))
#plt.legend( (p1[0], p2[0]), ('Previous Study', 'This Study'), 4 )
#plt.normalize
#plt.register_cmap(name='fu',cmap='jet',data='p3')
#m = get_cmap('RdBu')
p3.axis([-50,200,0,6])
p3.set_yticklabels(yticks, ha='left')
plt.draw()
yax = p3.get_yaxis()
pad = max(T.label.get_window_extent().width for T in yax.majorTicks)
yax.set_tick_params(pad=pad)

#plt.colormaps(plt.cm.get_cmap('RdBu'))
#plt.imshow(cmap='jet',position= oldMeans)
#plt.colorbar()

#imshow(cmap=get_cmap(m))
plt.tight_layout()
plt.draw()
plt.colormaps()
plt.show()