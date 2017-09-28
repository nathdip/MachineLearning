#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:14:49 2017

@author: atlas
"""

from numpy import*

def sigmoid(z):
    
    return 1/(1+exp(-z))
    
    
def costandGradient(X,y,theta,lregularize):
    
    y=matrix.transpose(array([y]))
    m=len(y)
    z=dot(X,theta)
    cost=-y*sigmoid(z)-(1-y)
    
    