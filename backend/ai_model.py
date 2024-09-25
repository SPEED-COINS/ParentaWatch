import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import os

def detect_unusual_activity(activity_log):
    # Load the secret key from environment variables
    secret_key = os.getenv('SECRET_KEY')

    if not secret_key:
        raise ValueError("Secret key not found! Please set the SECRET_KEY environment variable.")

    # Example of how the key might be used (this could be an API call, etc.)
    print(f"Using secret key: {secret_key}")

    # Load the trained model for activity monitoring
    try:
        model = tf.keras.models.load_model('activity_monitor_model.h5')
    except Exception as e:
        raise RuntimeError(f"Error loading the model: {e}")

    # Preprocess the activity log data
    activity_data = MinMaxScaler().fit_transform(activity_log)

    # Perform prediction
    prediction = model.predict(activity_data)

    # Check if the prediction exceeds the threshold for unusual activity
    if prediction > 0.8:  # Assuming 0.8 as the threshold
        return True
    return False

# Example usage (activity_log would be your actual input data)
activity_log = [[1, 2], [3, 4], [5, 6]]  # Replace this with real data
result = detect_unusual_activity(activity_log)
print(f"Unusual activity detected: {result}")
