# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:45:55 2017

@author: nath

"""
import glob,os
import glob,os
import time
#import recursive
from scipy.signal import butter,iirfilter,freqz,filtfilt,lfilter,cheby1
from scipy.integrate import simps
from scipy.optimize import curve_fit,least_squares
from scipy.stats import chisquare
import scipy.optimize as opt
import matplotlib.pyplot as plt
#import allantools as allan
import math
from numpy import*
from plotFunction import*

datafiles=glob.glob('*.txt')


set1= open(datafiles[0], 'r')
data_set1=loadtxt(set1, delimiter=',')

X=data_set1[:,0:2]
y=data_set1[:,2]

# visualize data
plt.figure('Data Visualization',figsize=(12,9))
plt.clf()

plotData(X,y)#defined in the module plotFunction
