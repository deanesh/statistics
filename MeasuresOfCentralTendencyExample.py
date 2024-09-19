import statistics
'''
Explanation of Measures:
Mean: Average of dataset, sum all values and dividing by total count of values.
Median: Middle value when dataset is sorted. If there's an even number of observations, 
it averages the two middle values.
Mode: Value that appears most frequently in dataset.
'''
# Sample data
data = [10, 20, 20, 30, 40, 50, 50, 50, 60]

# Calculate measures of central tendency
mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode(data)

# Display results
print(f"Data: {data}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
