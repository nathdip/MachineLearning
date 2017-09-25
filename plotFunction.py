# -*- coding: utf-8 -*-
"""
Spyder Editor

author@nath

This program is for plotting the classified data for visualization
"""
from numpy import*

def plotData(X,y):
    
    plus_indices=where(y==1)
    cross_indices=where(y==0)
    plus_indices=plus_indices[0]
    cross_indices=cross_indices[0]
    
    
    
    
    