from sklearn.ensemble import RandomForestClassifier

class SoilMoistureMachineLearningModel:
    def __init__(self):
        self.model = None

    def train_model(self, X_train, y_train):
        # Initialize and train the Random Forest classifier
        self.model = RandomForestClassifier(random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, features):
        # Make predictions using the trained model
        predictions = self.model.predict(features)
        return predictions
