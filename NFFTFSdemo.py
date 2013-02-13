import numpy as np
from pylab import *

nfftl = [1024,2048]
fsl = [100,200]

pxxl = []
freqsl = []
namel = []



for nfft in nfftl:
	for fs in fsl:
		name = "nfft = %d fs = %.1f" % (nfft, fs)
		namel.append (name)
		dt= 1.0/fs
		t = arange(0,10,dt)
		nse = randn(len(t))
		r = exp(-t/0.05)
		peak = 4
		cnse = convolve(nse, r)*dt
		cnse = cnse[:len(t)]
		s = 0.1*sin(2*pi*t*peak) + cnse
		(pxx, freqs) = psd(s,nfft,fs)
		pxxl.append(pxx)
		freqsl.append(freqs)


plt.clf()

print namel

subplot (211)
for i in range(len(namel)):
	name = namel[i]
	freqs = freqsl[i]
	pxx = pxxl[i]
	plot (freqs, pxx, label = name)
	plt.yscale('log')
	plt.legend(prop = {"size":7}, ncol = len(namel)).get_frame().set_alpha(0.5)
	ylabel ("power")
	xlabel ("Frequency (hz)")
subplot (212)
for i in range(len(namel)):
	name = namel[i]
	freqs = freqsl[i]
	pxx = pxxl[i]
	plot (freqs, pxx, label = name)
	plt.yscale('log')
	xlim([3,5])
	plt.legend(prop = {"size":7}, ncol = len(namel)).get_frame().set_alpha(0.5)
	ylabel ("Power")
	xlabel ("Frequency (hz)")
savefig('example 9.jpg')
show()


