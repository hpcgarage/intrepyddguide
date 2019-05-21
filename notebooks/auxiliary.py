#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
mpl.rc("savefig", dpi=100) # Adjust for higher-resolution figures

def gen_mixture_of_gaussians(centers, covars, m):
    from numpy.random import multivariate_normal, permutation
    k, d = centers.shape
    assert covars.shape[0] == k, "Number of covariance matrices ({}) does not match the number of centers ({}).".format(covars.shape[0], k)
    assert covars.shape[1] == d and covars.shape[2] == d, "Covariance matrices must be {} x {}, not {} x {}.".format(d, d, covars.shape[1], covars.shape[2])
    X = np.empty((m*k, d))
    y = np.empty(m*k, dtype=int)
    for i in range(k):
        mu = centers[i, :]
        sigma = covars[i, :, :]
        X[i*m:(i+1)*m, :] = multivariate_normal(mu, sigma, size=m)
        y[i*m:(i+1)*m] = i
    p = permutation(m*k)
    return X[p, :], y[p]

def labeled_points_to_df(points, labels, var_base=1):
    n, d = points.shape
    assert len(labels) == n, "Number of labels ({}) does not match the number of points ({}).".format(len(labels), n)
    cols = dict()
    for i in range(d):
        name = 'x_{}'.format(var_base+i)
        vals = points[:, i]
        cols[name] = vals
    cols['label'] = labels
    return pd.DataFrame(data=cols)

def make_scatter_plot(df, x="x_1", y="x_2", hue="label",
                      palette={0: "red", 1: "olive"},
                      size=5,
                      centers=None):
    sns.lmplot(x=x, y=y, hue=hue, data=df, palette=palette,
               fit_reg=False)
    if centers is not None:
        plt.scatter(centers[:,0], centers[:,1],
                    marker=u'*', s=500,
                    c=[palette[0], palette[1]])
    plt.show()

def visualize_clusters(points, labels):
    df = labeled_points_to_df(points, labels)
    make_scatter_plot(df)
    
def mark_matches(a, b, exact=False):
    """
    Given two Numpy arrays of {0, 1} labels, returns a new boolean
    array indicating at which locations the input arrays have the
    same label (i.e., the corresponding entry is True).
    
    This function can consider "inexact" matches. That is, if `exact`
    is False, then the function will assume the {0, 1} labels may be
    regarded as the same up to a swapping of the labels. This feature
    allows
    
      a == [0, 0, 1, 1, 0, 1, 1]
      b == [1, 1, 0, 0, 1, 0, 0]
      
    to be regarded as equal. (That is, use `exact=False` when you
    only care about "relative" labeling.)
    """
    assert a.shape == b.shape
    a_int = a.astype(dtype=int)
    b_int = b.astype(dtype=int)
    all_axes = tuple(range(len(a.shape)))
    assert ((a_int == 0) | (a_int == 1)).all()
    assert ((b_int == 0) | (b_int == 1)).all()
    
    exact_matches = (a_int == b_int)
    if exact:
        return exact_matches

    assert exact == False
    num_exact_matches = np.sum(exact_matches)
    if (2*num_exact_matches) >= np.prod(a.shape):
        return exact_matches
    return exact_matches == False # Invert
    
def count_matches(a, b, exact=False):
    """
    Given two sets of {0, 1} labels, returns the number of mismatches.
    
    This function can consider "inexact" matches. That is, if `exact`
    is False, then the function will assume the {0, 1} labels may be
    regarded as similar up to a swapping of the labels. This feature
    allows
    
      a == [0, 0, 1, 1, 0, 1, 1]
      b == [1, 1, 0, 0, 1, 0, 0]
      
    to be regarded as equal. (That is, use `exact=False` when you
    only care about "relative" labeling.)
    """
    matches = mark_matches(a, b, exact=exact)
    return np.sum(matches)


from PIL import Image
from matplotlib.pyplot import imshow

def read_img(path):
    """
    Read image and store it as an array, given the image path. 
    Returns the 3 dimensional image array.
    """
    img = Image.open(path)
    img_arr = np.array(img, dtype='int32')
    img.close()
    return img_arr

def display_image(arr):
    """
    display the image
    input : 3 dimensional array
    """
    arr = arr.astype(dtype='uint8')
    img = Image.fromarray(arr, 'RGB')
    imshow(np.asarray(img))
    plt.show()
    

# eof
