# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:24:54 2020

@author: dingxu
"""

import numpy as np
import matplotlib.pylab as plt
# Import pyTiming
from PyAstronomy.pyTiming import pyPeriod
from scipy.fftpack import fft,ifft
import seaborn
# Create some evenly sampled artificial data (Poisson noise)
data = np.loadtxt('datamag.txt')
#time = np.arange(0,119,0.1)
time = data[:,0:1]-np.min(data[:,0:1])
flux = data[:,1:2]

yy = fft(flux) 
yreal = yy.real
yimag = yy.imag 

yf=abs(fft(flux))

yf1=abs(fft(flux))/len(time) 
yf2 = yf1[range(int(len(time)/2))]


xf = np.arange(len(flux))        # 频率
xf1 = xf
xf2 = xf[range(int(len(time)/2))]  #取一半区间


plt.subplot(221)
plt.plot(time, flux, 'bp')   
plt.title('Original wave')

plt.subplot(222)
plt.plot(xf,yf,'r')
plt.title('FFT of Mixed wave(two sides frequency range)',fontsize=7,color='#7A378B')  #注意这里的颜色可以查询颜色代码表

plt.subplot(223)
plt.plot(xf1,yf1,'g')
plt.title('FFT of Mixed wave(normalization)',fontsize=9,color='r')

plt.subplot(224)
plt.plot(xf2,yf2,'b')
plt.title('FFT of Mixed wave)',fontsize=10,color='#F08080')



from astropy.time import Time

time1 = ['2019-10-20T10:50:42']
t1 = Time(time1, format='isot', scale='utc')

time2 = ['2019-10-24T16:12:14.0']
t2 = Time(time2, format='isot', scale='utc')


print(t2.jd[0]-t1.jd[0])