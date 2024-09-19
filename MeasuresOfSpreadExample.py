import statistics
'''
Explanation of Measures:
Mean: Average of the dataset.
Variance: Measures how far each number in the dataset is from the mean, squared.
Standard Deviation: Square root of variance, 
providing a measure of spread in the same unit as the data.
Range: Difference between the maximum and minimum values in the dataset.
Interquartile Range (IQR): The difference between the first (Q1) and third (Q3) quartiles,
 measuring the spread of the middle 50% of the data.
'''

# Sample data
data = [10, 20, 20, 30, 40, 50, 50, 50, 60]

# Calculate measures of spread
mean_value = statistics.mean(data)
variance_value = statistics.variance(data)
std_deviation_value = statistics.stdev(data)

# Range
data_range = max(data) - min(data)

# Interquartile Range (IQR)
q1 = statistics.quantiles(data, n=4)[0]  # First quartile
q3 = statistics.quantiles(data, n=4)[2]  # Third quartile
iqr = q3 - q1

# Display results
print(f"Data: {data}")
print(f"Mean: {mean_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_deviation_value}")
print(f"Range: {data_range}")
print(f"Interquartile Range (IQR): {iqr}")
