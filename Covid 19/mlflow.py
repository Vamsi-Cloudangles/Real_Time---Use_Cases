import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import warnings
import sys
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler