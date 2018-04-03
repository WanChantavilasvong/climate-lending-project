import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from itertools import cycle, islice
%matplotlib inline

hmda = pd.read_csv('Data/hmda_data.csv', sep=',', low_memory=False)
hmda.shape

## Problem 1: Create a Bar Chart of Total Activity by Day
loanbylender = hmda.groupby('panel_name')['loan_amount'].sum().to_frame(name = 'loan_amount')
loanbylender = loanbylender.sort_values('loan_amount', ascending=False)
loanbylender

loanbylender.to_csv('Data/loan-by-lender.csv', sep=',', encoding='utf-8')
