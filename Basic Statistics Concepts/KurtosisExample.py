import pandas as pd
'''
Kurtosis measures the "tailedness" of the probability distribution.
High kurtosis indicates heavy tails and a peaked distribution, 
while low kurtosis indicates light tails and a flatter distribution. 
In machine learning, kurtosis helps in understanding 
the distribution's extremities and potential outliers.
'''
# Sample data
data = pd.Series([10, 12, 23, 23, 16, 23, 21, 16, 40])

# Calculate kurtosis
kurt_value = data.kurtosis()

print("Data:\n", data)
print("Kurtosis (pandas):", kurt_value)
