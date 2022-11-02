import pandas as pd
import numpy as np
import os


def preporations(name):
	df = pd.read_csv(name)
	return np.array(df)