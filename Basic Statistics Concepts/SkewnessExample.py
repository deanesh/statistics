import pandas as pd
'''
Skewness measures the asymmetry of the probability distribution of a dataset. 
+ve skewness indicates that the tail on the right side of the distribution is longer 
or fatter, while -ve skewness indicates that tail on left side is longer or fatter. 
Helps in understanding distribution shape and making transformations to meet model assumptions.
'''
# Sample data
data = pd.Series([10, 12, 23, 23, 16, 23, 21, 16, 40])

# Calculate skewness
skewness = data.skew()

print("Data:\n", data)
print("Skewness (pandas):", skewness)
