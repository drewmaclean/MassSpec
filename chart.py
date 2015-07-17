#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


oldMeans = [0,1,4,8,8,8]
newMeans = [2,3,6,7,8,6]

#oldStd     = (2, 3, 4, 1, 2, 1)
#newStd   = (3, 5, 2, 3, 3, 2)
ind = np.arange(len(oldMeans))    # the x locations for the groups
width = .55       # the width of the bars: can also be len(x) sequence

p1 = plt.barh(ind, oldMeans, width, color='b')#, bottom=(0,0,0,0,0,0)) #yerr=newStd
p2 = plt.barh(ind+.25, newMeans, width, color='y')#, bottom=(0,0,0,0,0,0)) #yerr=oldStd

plt.xlabel('No. of identified proteins')
plt.title('Identified proteins by fmol')
plt.yticks(ind+width/2., ('0.5 fmol', '5 fmol', '50 fmol', '500 fmol', '5,000 fmol', '50,000 fmol') )
plt.xticks(np.arange(0,10,1))
plt.legend( (p1[0], p2[0]), ('Previous Study', 'This Study'), 4 )

plt.show()