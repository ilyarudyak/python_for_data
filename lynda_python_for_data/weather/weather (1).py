#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:09:56 2016

@author: ilyarudyak
"""

import numpy as np

# stations = {'AE000041196': 'SHARJAH INTER. AIRP GSN 41196', ... }
stations = {}
for line in open('stations.txt', encoding='latin1'):
    if 'GSN' in line:
        fields = line.split()
        stations[fields[0]] = ' '.join(fields[4:]) 
        
def findstation(s):
    found = {code: name for code, name in stations.items() if s in name}
    print(found)
    
datastations = ['USW00022536','USW00023188','USW00014922','RSM00030710']

# get temperatures from these stations
def parsefile(filename):
    return np.genfromtxt(filename,
                         delimiter = dly_delimiter,
                         usecols = dly_usecols,
                         dtype = dly_dtype,
                         names = dly_names)
    
dly_delimiter = [11,4,2,4] + [5,1,1,1] * 31
dly_usecols = [1,2,3] + [4*i for i in range(1,32)]
dly_dtype = [np.int32,np.int32,(np.str_,4)] + [np.int32] * 31
dly_names = ['year','month','obs'] + [str(day) for day in range(1,31+1)]





















