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
from CostFunctionandGradient import*

datafiles=glob.glob('*.txt')


set1= open(datafiles[0], 'r')
data_set1=loadtxt(set1, delimiter=',')

X=data_set1[:,0:2]
y=data_set1[:,2]

# visualize data
plt.figure('Data Visualization',figsize=(12,9))
plt.clf()

plotData(X,y)#defined in the module plotFunction

#adding the intercept to the X data



intercept=ones((len(y),1))

X_new=hstack((intercept, X))
m,n=X_new.shape

#initialize theta

theta_init=zeros((n,1))

test_theta = array([[-24],[0.2],[0.2]])

cost_test=cost(test_theta, X_new, y)
gradient_test=gradient(test_theta, X_new, y)

#print('The cost is : ', cost_test,'the gradient is: ',gradient_test)

#Optimization using fmin_bfgs

#theta,cost= opt.fmin_ncg(cost,x0=theta_init,fprime=gradient,args=(X_new,y),maxiter=None)
result=opt.minimize(fun=cost, x0 = theta_init, args = (X_new,y),method = 'BFGS',jac = gradient,options={'disp':True,'maxiter':400});

theta=result.x
print('The optimized theta without regularization is: ', theta)
theta=theta.reshape((n,1))
predict=array([[1],[45],[85]])
print('For a student with marks 45 and 85 we predict a acceptance probability of ',ndarray.flatten(sigmoid(dot(matrix.transpose(theta),predict))))