```python
# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    def __init__(self, data):
        self.data = pd.read_csv(data)

    def handle_missing_values(self):
        # Fill missing values with mean
        self.data.fillna(self.data.mean(), inplace=True)

    def handle_outliers(self, method='z-score'):
        # Handle outliers using Z-score method
        if method == 'z-score':
            z_scores = (self.data - self.data.mean()) / self.data.std()
            self.data = self.data[(z_scores < 3).all(axis=1)]
        # Handle outliers using IQR method
        elif method == 'iqr':
            Q1 = self.data.quantile(0.25)
            Q3 = self.data.quantile(0.75)
            IQR = Q3 - Q1
            self.data = self.data[~((self.data < (Q1 - 1.5 * IQR)) | (self.data > (Q3 + 1.5 * IQR))).any(axis=1)]

    def feature_scaling(self, method='standardization'):
        # Perform feature scaling using Standardization
        if method == 'standardization':
            scaler = StandardScaler()
            self.data = pd.DataFrame(scaler.fit_transform(self.data), columns=self.data.columns)
        # Perform feature scaling using Min-Max Scaling
        elif method == 'min-max':
            scaler = MinMaxScaler()
            self.data = pd.DataFrame(scaler.fit_transform(self.data), columns=self.data.columns)

    def data_splitting(self, test_size=0.2, random_state=42):
        # Split the data into training and testing sets
        train_data, test_data = train_test_split(self.data, test_size=test_size, random_state=random_state)
        return train_data, test_data

# Usage
preprocessor = DataPreprocessor('data.csv')
preprocessor.handle_missing_values()
preprocessor.handle_outliers('z-score')
preprocessor.feature_scaling('standardization')
train_data, test_data = preprocessor.data_splitting()
```
