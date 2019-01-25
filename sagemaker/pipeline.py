import pandas as pd
import numpy as np
import random


def get_data(k=100):
    return pd.DataFrame({'x': np.random.uniform(0, 1, size=k),
                         'y': random.choices(['class1', 'class2'], k=k)})
