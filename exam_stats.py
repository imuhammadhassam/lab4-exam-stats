import pandas as pd
import numpy as np
from scipy import stats

# Exam scores of 10 students
scores = pd.Series([
    72, 65, 88, np.nan, 54,
    91, 76, np.nan, 83, 69
])

print("Original Scores:")
print(scores)

print("\nDescriptive Statistics:")
print(scores.describe())

clean_scores = scores.dropna()

print("\nSkewness:", stats.skew(clean_scores))
print("Kurtosis:", stats.kurtosis(clean_scores))

missing_values = scores.isnull().sum()
print("\nMissing values:", missing_values)

mean_score = scores.mean()
filled_scores = scores.fillna(mean_score)

print("\nMean used to fill missing values:", mean_score)
print("\nFilled Scores:")
print(filled_scores)