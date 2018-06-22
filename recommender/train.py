#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__author__ = "Loreto Parisi"
__copyright__ = "Copyright 2018, Loreto Parisi"
__credits__ = ["Loreto Parisi"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Loreto Parisi"
__email__ = "loretoparisi@gmail.com"
'''
import os
import turicreate as tc

DATASET_ROOT='/Users/loretoparisi/webservice/'

actions = tc.SFrame.read_csv(os.path.join(DATASET_ROOT,"ml-20m","ratings.csv"))
items = tc.SFrame.read_csv(os.path.join(DATASET_ROOT,"ml-20m","movies.csv"))


