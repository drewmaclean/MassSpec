#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
import math


oldMeans = [0,1,4,8,8,8]
newMeans = [2,3,6,7,8,6]
change = []

#oldStd     = (2, 3, 4, 1, 2, 1)
#newStd   = (3, 5, 2, 3, 3, 2)
ind = np.arange(len(oldMeans))    # the x locations for the groups
width = .55       # the width of the bars: can also be len(x) sequence

for i in range(len(oldMeans)):
    try:
        change.append((newMeans[i] / oldMeans[i] - 1) * 100)
    except:
        change.append(100.0)


p1 = plt.barh(ind, change, width, color='c')#, bottom=(0,0,0,0,0,0)) #yerr=newStd
#p2 = plt.barh(ind+.25, newMeans, width, color='y')#, bottom=(0,0,0,0,0,0)) #yerr=oldStd

plt.xlabel('Percent change in No. of identified proteins')
plt.title('Percent change between studies')
plt.yticks(ind+width/2., ('0.5 fmol', '5 fmol', '50 fmol', '500 fmol', '5,000 fmol', '50,000 fmol') )
plt.xticks(np.arange(-50,max(i for i in change),25))
#plt.legend( (p1[0], p2[0]), ('Previous Study', 'This Study'), 4 )
plt.set_cmap('bone')
plt.axis([-50,200,0,6])

plt.tight_layout()
plt.show()