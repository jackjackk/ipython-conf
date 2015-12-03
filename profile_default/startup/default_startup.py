# OS libraries
import os
import glob
import sys
import subprocess as sproc


# Core scientific libraries
import numpy as np
import scipy as sp
import pandas as pd


# Machine learning libraries
import sklearn as sk
import sklearn.cluster as skc
import sklearn.datasets as skd
import sklearn.metrics as skm
import sklearn.preprocessing as skp
import sklearn.pipeline as skpip
import sklearn.decomposition as skdecomp
import sklearn.gaussian_process as skgp


# Statistics libraries
import patsy as pa
import scipy.signal as sps
import statsmodels.formula.api as smf


# Utilities libraries
from sklearn.externals import joblib
from pprint import pprint
import time
import re
import logging as lg
import itertools as it
import pdb


# GAMS & WITCH
import gdxpy as gp
import witchpy as w
import sspdb as ssp


# Auxiliary functions


def cdhome(x):
    """CD to $HOME/``x``."""
    cdpathlist = [os.environ['HOME'], ] + x.split('/')
    os.chdir(os.path.join(*cdpathlist))
