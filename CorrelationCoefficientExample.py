import pandas as pd
'''
A correlation coefficient measures the strength and direction of linear relationship 
between two variables. Values range from -1 to 1, 
1/-1/0 indicates a perfect +ve/-ve/no linear relationship 
It is important in feature selection to understand relationships between features
'''
# Sample data
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

# Calculate correlation coefficient
correlation_coefficient = df['x'].corr(df['y'])

print("Correlation Coefficient (pandas):", correlation_coefficient)
