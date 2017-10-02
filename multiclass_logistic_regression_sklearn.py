#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 14:55:24 2017

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
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
import scipy.io as scipo
from  skimage import*
from time import sleep
datafiles=glob.glob('*.mat')

set_1=scipo.loadmat(datafiles[0])
set_2=scipo.loadmat(datafiles[1])

keys_set_1=[]
for key in set_1:
    keys_set_1.append(key)
    
X=set_1[keys_set_1[3]]
y=ndarray.flatten(set_1[keys_set_1[4]])

no_images_display=25
X_display=X[0:no_images_display]

temp=reshape(X_display[1],(20,20))
plt.figure('Example')
plt.imshow(temp,cmap='gray')

image_classifier=LogisticRegression(C=100)
image_classifier=image_classifier.fit(X,y)
print('The accuracy is:',image_classifier.score(X,y))

for i in range(400,600):
    plt.figure()
    plt.clf()
    X_new=X[i:i+1]
    temp=reshape(X_new,(20,20))
    plt.imshow(temp,cmap="gray")
    plt.show()
    print(image_classifier.predict(X_new))
    

