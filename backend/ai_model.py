import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

def detect_unusual_activity(activity_log):
    model = tf.keras.models.load_model('activity_monitor_model.h5')
    activity_data = MinMaxScaler().fit_transform(activity_log)
    prediction = model.predict(activity_data)
    if prediction > 0.8:  # Threshold for unusual activity
        return True
    return False
