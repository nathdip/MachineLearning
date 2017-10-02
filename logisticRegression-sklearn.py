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
from sklearn.preprocessing import PolynomialFeatures


datafiles=glob.glob('*.txt')


set1= open(datafiles[0], 'r')
set2=open(datafiles[1],'r')
data_set1=loadtxt(set1, delimiter=',')
data_set2=loadtxt(set2,delimiter=',')
X_1=data_set1[:,0:2]
y_1=data_set1[:,2]

X_2=data_set2[:,0:2]
y_2=data_set2[:,2]

plotData(X_2,y_2)#defined in the module plotFunction
poly=PolynomialFeatures(6)

X_transformed=poly.fit_transform(X_2)





model1=LogisticRegression(C=4)
model1=model1.fit(X_1,y_1)
print(model1.score(X_1,y_1))

model2=LogisticRegression(C=10)
model2=model.fit(X_transformed,y_2)
print(model2.score(X_transformed,y_2))
