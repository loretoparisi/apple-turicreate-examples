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

# we use the MovieLens 20M dataset
actions = tc.SFrame.read_csv(os.path.join(DATASET_ROOT,"ml-20m","ratings.csv"))

print( actions[0:10] )

# You may have additional data about users or items. For example we might have a dataset of movie metadata.
items = tc.SFrame.read_csv(os.path.join(DATASET_ROOT,"ml-20m","movies.csv"))

print( items[0:10] )

# First we create a random split of the data to produce a validation set that can be used to evaluate the model.
training_data, validation_data = tc.recommender.util.random_split_by_user(actions, 'userId', 'movieId')
model = tc.recommender.create(training_data, 'userId', 'movieId')

# The input parameter k controls how many items to recommend for each user.
k=5

# Now that you have a model, you can make recommendations
top_recommendations = model.recommend(k=k)

# print first (k*3) rows ( k results x 3 users) of 4 columns
num_users=3
top_recommendations.print_rows(num_rows=(k*num_users), num_columns=4)

# The user names must correspond to strings in the user_id column in the training data.
recommendations = {}
recommendations['1'] = model.recommend(users=['1'])
recommendations['2'] = model.recommend(users=['2'])

# print recommendations by user
for r in recommendations:
    recommendations[r].print_rows(num_rows=k, num_columns=4)


