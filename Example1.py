#!/usr/bin/env python
# python

from pylab import *

fs = 100
dt = 1.0/fs
t = arange(0,10,dt)
nse = randn(len(t))
r = exp(-t/0.05)
k = 2

cnse = convolve(nse, r)*dt #The following creates sample data.
cnse = cnse[:len(t)]
s = 0.1*sin(2*k*pi*t) + cnse #s is the sample data created

subplot(211)
plot(t,s) #This simply plots s
subplot(212)
psd(s, 512, fs) #This runs the Fourier Transform.
axvline(x=k, color = 'red') #Notice that the frequency of the graph sin(2*pi*t) is 1. 
#This is why the vertical line is at x = 1.
#to Create the second figure, uncomment the text below
#xlim([0,10])

show()

