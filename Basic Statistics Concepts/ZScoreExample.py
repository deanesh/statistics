import pandas as pd
'''
A z-score measures how many standard deviations a data point is from the mean.
It is used to standardize data and to identify outliers. In machine learning,
z-scores can be used for feature scaling to ensure that features contribute equally 
to the model.
'''
# Sample data
data = pd.Series([10, 12, 23, 23, 16, 23, 21, 16])

# Calculate z-scores
z_scores = (data - data.mean()) / data.std()

print("Data:\n", data)
print("Z-scores:\n", z_scores)
