#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:10:57 2016

@author: ilyarudyak
"""
import matplotlib.pyplot as plt
import numpy as np

population = np.loadtxt('world_population.txt', dtype=('i4', 'i4'))
plt.plot(population[:,0], population[:,1])
