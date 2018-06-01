# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 22:28:58 2018

@author: xuc
"""

import sys
import numpy as np

# file_dir: training file and testing file should put at the same directory
def load_data(dirname, normalization = False, slice_ratio = 1):
    training_file = dirname + '/' + 'TRAIN.csv';
    testing_file = dirname + '/' + 'TEST.csv'
    print training_file
    print testing_file
    
    Training_data = np.loadtxt(training_file, dtype=np.str, delimiter=",")
    Testing_data = np.loadtxt(training_file, dtype=np.str, delimiter=",");
    
    
    return 1   