#!/usr/local/bin/python

import sys
import math
import matplotlib.pyplot as plt
from numpy.random import *
from comp import Comp
from decomp import Decomp
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

# A + B -(k1)-> C
# C -(k2)-> A + B
t = 0.0
tend = 1.0
s = [0, 0, 1000]
k = [0.01, 5]
events = [Comp(t, s, k), Decomp(t, s, k)]

sys.stdout.write(GREEN+"{0:>8}".format("time")+ENDC)
sys.stdout.write(GREEN+"{0:>8}".format("A")+ENDC)
sys.stdout.write(GREEN+"{0:>8}".format("B")+ENDC)
sys.stdout.write(GREEN+"{0:>8}".format("C")+ENDC)
print
sys.stdout.write(YELLOW+"{0:>8}".format(t)+ENDC)
sys.stdout.write("{0:>8}".format('%d' % (s[0])))
sys.stdout.write("{0:>8}".format('%d' % (s[1])))
sys.stdout.write("{0:>8}".format('%d' % (s[2])))
print

#Logger
otime = [t]
adata = [s[0]]
bdata = [s[1]]
cdata = [s[2]]

#newt, news <- t, s, events
def step(t, s, events):

    atotal = 0
    alist = []
    for i in range(len(events)):
        atotal += events[i].propensity(s)
        alist.append(events[i].propensity(s))

    tau = float((1/atotal)*math.log1p(1/rand()))
    newt = t + tau

    a0, l = 0, 0
    r = rand()*atotal
    for a in alist:
        a0 += a
        if a0 > r:
            j = l 
        else:
            l += 1
                    
    news = events[j].execute(s)
    events[j].showdata(newt, news)
    otime.append(newt)
    adata.append(news[0])
    bdata.append(news[1])
    cdata.append(news[2])
    return newt, news

while t <= tend:
    t, s = step(t, s, events)

plt.plot(otime,cdata)
plt.plot(otime,adata)
plt.show()

