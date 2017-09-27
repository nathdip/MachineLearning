#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:14:49 2017

@author: atlas
"""
def sigmoid(z):
    
    return 1/(1+exp(-z))
    
    
def costandGradient(X,y,theta,lregularize):
    
    m=len(y)
    z=X.theta
    J=sum
    
    