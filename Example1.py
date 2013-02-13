#!/usr/bin/env python
# python

from pylab import *

fs = 100 #calculate sampling frequency
dt = 1.0/fs 
t = arange(0,10,dt) #The domain of the function is from 0 to 10
nse = randn(len(t)) #adds noise
r = exp(-t/0.05)
k = 2

cnse = convolve(nse, r)*dt #The following creates a little bit of noise
cnse = cnse[:len(t)]
s = 0.1*sin(2*k*pi*t) + cnse #This generates a sine wave on top of noise

subplot(211)
plot(t,s) #This plots s in the top panel.
subplot(212)
psd(s, 512, fs) #This runs the Fourier Transform.
axvline(x=k, color = 'red') #Notice that the frequency of the graph sin(2*pi*k*t) is k. 
#This is why the vertical line is at x = k.
#to Create the second figure, uncomment the text below
#xlim([0,10]) #This zooms in on the figure.

show()

