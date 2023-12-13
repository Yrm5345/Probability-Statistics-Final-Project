from components.plant_feature_engineering import PlantFeatureEngineering
from components.soil_moisture_machine_learning_model import SoilMoistureMachineLearningModel
from components.soil_moisture_bayesian_inference import SoilMoistureBayesianInference

class IntelligentWateringSystem:
    def __init__(self):
        # Initialize components
        self.feature_engineering = PlantFeatureEngineering()
        self.ml_model = SoilMoistureMachineLearningModel()
        self.bayesian_inference = SoilMoistureBayesianInference()

    def train_system(self, raw_data, labels):
        # Feature engineering
        features = self.feature_engineering.process_data(raw_data)

        # Train machine learning model
        self.ml_model.train_model(features, labels)

    def predict_and_water(self, new_data):
        # Feature engineering for new data
        features = self.feature_engineering.process_data(new_data)

        # Predict using machine learning model
        ml_predictions = self.ml_model.predict(features)

        # Bayesian inference
        bayesian_posterior = self.bayesian_inference.calculate_posterior(new_data)

        # Combine machine learning and Bayesian predictions
        integrated_probability = (bayesian_posterior + ml_predictions) / 2

        # Threshold-based decision
        threshold = 0.6  # --> THIS COULD 
        if integrated_probability > threshold:
            print('Water the plants')
        else:
            print('Do not water the plants')

