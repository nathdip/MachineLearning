# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 21:15:32 2017

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
from sklearn.neural_network import MLPClassifier
import scipy.io as scipo
from  skimage import*
from time import sleep
datafiles=glob.glob('*.mat')

set_1=scipo.loadmat(datafiles[0])

keys_set_1=[]
for key in set_1:
    keys_set_1.append(key)
    
X=set_1[keys_set_1[3]]
y=ndarray.flatten(set_1[keys_set_1[2]])

image_classifier=MLPClassifier(hidden_layer_sizes=(10,25 ),activation='logistic',solver='lbfgs',alpha=1)
image_classifier=image_classifier.fit(X,y)
print(image_classifier.score(X,y))
n_rand=random.randint(0,4999,50)
for i in n_rand:
    plt.figure()
    plt.clf()
    X_new=X[i:i+1]
    temp=reshape(X_new,(20,20))
    image_label=image_classifier.predict(X_new)
    plt.imshow(temp,cmap="gray")
    plt.text(2.5,2.5,str(image_label),color='red')
    plt.show()
    print(image_classifier.predict(X_new))
