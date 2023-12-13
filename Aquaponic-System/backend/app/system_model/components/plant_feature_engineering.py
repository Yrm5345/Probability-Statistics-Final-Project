import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class FeatureEngineering:
    def __init__(self, n_samples=10000, moisture_threshold=0.5, test_size=0.2, random_state=42):
        self.n_samples = n_samples
        self.moisture_threshold = moisture_threshold
        self.test_size = test_size
        self.random_state = random_state
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def generate_synthetic_data(self):
        data = {
            'weather_condition': np.random.choice(['Sunny', 'Cloudy', 'Rainy'], p=[0.4, 0.4, 0.2], size=self.n_samples),
            'plant_type': np.random.choice(['Cactus', 'Fern', 'Rose'], p=[0.3, 0.4, 0.3], size=self.n_samples),
            'TSLW': [max(1, int(np.random.normal(15, 5))) for _ in range(self.n_samples)],
            'temperature': np.random.normal(25, 5, self.n_samples),
            'humidity': np.random.normal(60, 10, self.n_samples),
            'sunlight_Duration': np.random.normal(10, 2, self.n_samples),
            'soil_Type': np.random.choice(['Sandy', 'Loamy', 'Clayey'], p=[0.3, 0.4, 0.3], size=self.n_samples),
            'plant_Size': np.random.normal(10, 3, self.n_samples),
            'wind_Speed': np.random.normal(5, 2, self.n_samples),
            'soil_moisture': np.random.uniform(0, 1, self.n_samples),
        }
        self.df = pd.DataFrame(data)

    def convert_to_binary_classification(self):
        self.df['soil_moisture_binary'] = (self.df['soil_moisture'] > self.moisture_threshold).astype(int)

    def one_hot_encoding(self):
        self.df = pd.get_dummies(self.df, columns=['weather_condition', 'plant_type', 'soil_Type'])

    def split_data(self):
        X = self.df.drop(['soil_moisture', 'soil_moisture_binary'], axis=1)
        y_binary = self.df['soil_moisture_binary']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y_binary, test_size=self.test_size, random_state=self.random_state
        )


