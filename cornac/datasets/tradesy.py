# -*- coding: utf-8 -*-

"""
@author: Quoc-Tuan Truong <tuantq.vnu@gmail.com>

Original data: http://jmcauley.ucsd.edu/data/tradesy/
This data is used in the VBPR paper. After cleaning the data, we have:
- Number of feedback: 394,421 (410,186 is reported but there are duplicates)
- Number of users:     19,243 (19,823 is reported due to duplicates)
- Number of items:    165,906 (166,521 is reported due to duplicates)

"""

from ..utils import cache
from ..data import reader
import numpy as np


def load_data():
    """Load the feedback observations

    Returns
    -------
    data: array-like
        Data in the form of a list of tuples (user, item, 1).

    """
    fpath = cache(url='https://static.preferred.ai/cornac/datasets/tradesy/users.zip',
                  unzip=True, relative_path='tradesy/users.csv')
    return reader.read_ui(fpath, sep=',')


def load_feature():
    """Load the item visual feature

    Returns
    -------
    features: numpy.ndarray
        Feature matrix with shape (n, 4096) with n is the number of items.

    item_ids: List
        List of item ids aligned with indices in `features`.
    """
    features = np.load(cache(url='https://static.preferred.ai/cornac/datasets/tradesy/item_features.zip',
                             unzip=True, relative_path='tradesy/item_features.npy'))
    fpath = cache(url='https://static.preferred.ai/cornac/datasets/tradesy/item_ids.zip',
                  unzip=True, relative_path='tradesy/item_ids.txt')
    with open(fpath, 'r') as f:
        item_ids = f.read().splitlines()
    return features, item_ids
