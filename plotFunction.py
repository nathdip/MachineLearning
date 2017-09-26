# -*- coding: utf-8 -*-
"""
Spyder Editor

author@nath

This program is for plotting the classified data for visualization
"""
from numpy import*
import matplotlib.pyplot as plt

def plotData(X,y):
    
    plus_indices=where(y==1)
    cross_indices=where(y==0)
    plus_indices=plus_indices[0]
    cross_indices=cross_indices[0]
    
    X1_plus=X[:,0][plus_indices]
    X2_plus=X[:,1][plus_indices]
    
    X1_cross=X[:,0][cross_indices]
    X2_cross=X[:,1][cross_indices]   
    
    plt.xlabel('Exam Score 1')
    plt.ylabel('Exam Score 2')
    
    plt.plot(X1_plus,X2_plus,'b+',markersize=10,label='Accepted')
    plt.plot(X1_cross,X2_cross,'kx',markersize=10,label='Rejected')
    plt.legend(loc='best')
    return plt.show()
    
   
    
    
    