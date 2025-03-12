import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Load dataset
def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess data
def preprocess_data(data):
    # Check for null values
    if data.isnull().sum().any():
        print("Null values found, filling with mean...")
        data = data.fillna(data.mean())
    
    # Standardize the features
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    return data_scaled, scaler

# Train Isolation Forest model
def train_isolation_forest(data):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(data)
    return model

# Predict anomalies
def predict_anomalies(model, data):
    predictions = model.predict(data)
    # Convert predictions to binary format: -1 (anomaly) and 1 (normal)
    predictions = np.where(predictions == -1, 1, 0)
    return predictions

# Plot results
def plot_results(data, predictions):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=predictions, palette=["blue", "red"], alpha=0.6)
    plt.title("Anomaly Detection using Isolation Forest")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend(title='Anomaly', loc='upper right')
    plt.show()

# Confusion matrix visualization
def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

# Main function to run the anomaly detection
def main(filepath, true_labels=None):
    data = load_data(filepath)
    
    if data is not None:
        data_scaled, scaler = preprocess_data(data)
        model = train_isolation_forest(data_scaled)
        predictions = predict_anomalies(model, data_scaled)
        
        # Plotting results
        plot_results(data_scaled, predictions)
        
        if true_labels is not None:
            plot_confusion_matrix(true_labels, predictions)

if __name__ == "__main__":
    # Example usage
    main('data/anomaly_data.csv', true_labels=None)
    
# Example synthetic data generation for testing (Uncomment to use)
# def generate_synthetic_data(n_samples=1000, n_features=2, n_inliers=950):
#     X = np.random.randn(n_samples, n_features)
#     # Introduce some anomalies
#     anomalies = np.random.uniform(low=-6, high=6, size=(n_samples - n_inliers, n_features))
#     X = np.vstack((X[:n_inliers], anomalies))
#     np.random.shuffle(X)
#     return X
# Uncomment below to create synthetic data
# np.savetxt('data/anomaly_data.csv', generate_synthetic_data(), delimiter=',')