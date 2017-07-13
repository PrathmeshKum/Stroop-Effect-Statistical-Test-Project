# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:42:21 2017

@author: Prathmesh
"""

# Program for creating visualization of Project 1

import matplotlib.pyplot as plt


# 1. For histogram of two conditions 

Bins=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
Congruent=[12.079,16.791,9.564,8.63,14.669,12.238,14.692,8.987,9.401,14.48,22.328,15.298,15.073,16.929,18.2,12.13,18.495,10.639,11.344,12.369,12.944,14.233,19.71,16.004]
Incongruent=[19.278,18.741,21.214,15.687,22.803,20.878,24.572,17.394,20.762,26.282,24.524,18.644,17.51,20.33,35.255,22.15,25.139,20.429,17.425,34.288,23.894,17.96,22.058,21.157]

plt.hist(Congruent, Bins, facecolor='blue', label='Congruent')
plt.hold(True)
plt.xlabel('Time Taken To Name Ink Colour')
plt.ylabel('Number Of Samples')
plt.title('Histogram For Both Conditions')
plt.hist(Incongruent, Bins, facecolor='red', label='Incongruent')
plt.legend(loc='upper left')
plt.xlim(0.0, 35)
plt.ylim(0.0, 8)
plt.show()

# 2. For histogram of the differences

Differences=[7.199,1.95,11.65,7.057,8.134,8.64,9.88,8.407,11.361,11.802,2.196,3.346,2.437,3.401,17.055,10.028,6.644,9.79,6.081,21.919,10.95,3.727,2.348,5.153]
plt.hist(Differences, Bins, facecolor='green', label='Differences')
plt.legend(loc='upper left')
plt.xlabel('Difference Between Time Taken To Name Ink Colour For 2 Condtions')
plt.ylabel('Number Of Samples')
plt.title('Histogram For Differences')
plt.xlim(0.0, 45)
plt.ylim(0.0, 5)
plt.show()