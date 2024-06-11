import pandas as pd
import numpy as np

data = {
    'A': ['cat', 'dog', 'bird', np.nan, 'dog'],
    'B': [1, 2, np.nan, 4, 5],
    'C': [5, 6, 7, 8, 9],
    'D': [10, np.nan, 12, 13, 14]
}

df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df, columns=['A'], dummy_na=True)

df_imputed = df.fillna(df.mean())

print("Original DataFrame:")
print(df)
print("\nDataFrame after one-hot encoding:")
print(df_encoded)
print("\nDataFrame after missing value imputation:")
print(df_imputed)
