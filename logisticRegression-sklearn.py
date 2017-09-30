#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:59:13 2017

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
from CostFunctionandGradient import*
from sklearn.linear_model import LogisticRegression


datafiles=glob.glob('*.txt')


set1= open(datafiles[0], 'r')
set2=open(datafiles[1],'r')
data_set1=loadtxt(set1, delimiter=',')

X_1=data_set1[:,0:2]
y_1=data_set1[:,2]

model=LogisticRegression(C=4)
model=model.fit(X,y)
print(model.score(X,y))