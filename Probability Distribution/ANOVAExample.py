import pandas as pd
import scipy.stats as stats

# Sample data (test scores for students from three schools)
data = {'School A': [85, 92, 78, 89, 95],
        'School B': [75, 80, 82, 77, 84],
        'School C': [90, 93, 88, 91, 96]}

df = pd.DataFrame(data)
f_statistic, p_value = stats.f_oneway(df['School A'], df['School B'], df['School C'])

print("F-statistic:", f_statistic)
print("p-value:", p_value)