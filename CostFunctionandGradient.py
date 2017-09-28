#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:14:49 2017

@author: atlas
"""

from numpy import*

def sigmoid(x):
    
    return 1/(1+exp(-x))
    
    
def cost(theta,X,y):
    
    
    m,n=X.shape
    y = y.reshape((m,1))
    theta=theta.reshape((n,1))
    z=dot(X,theta)
    h=sigmoid(z)
    cost=-y*log(h)-(1-y)*log(1-h)
    
    J=sum(cost)/m
    
    
    return J;

def gradient(theta,X,y):
    
    m,n=X.shape
    y = y.reshape((m,1))
    theta=theta.reshape((n,1))

    z=dot(X,theta)
    h=sigmoid(z)
    
    grad=dot(matrix.transpose(X),(h-y))/m
    return ndarray.flatten(grad)
