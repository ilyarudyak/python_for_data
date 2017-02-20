#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:46:33 2016

@author: ilyarudyak
"""

import matplotlib.pyplot as plt
import numpy as np


le_dtype = [('year', 'i4'), ('male', 'f4'), ('female', 'f4')]
le = np.loadtxt('life_expectancies_usa.txt', dtype=le_dtype, delimiter=',')
plt.plot(le['year'], le['male'], 'bo-', label='male')
plt.plot(le['year'], le['female'], 'go-', label='female')
plt.legend(loc='upper left')