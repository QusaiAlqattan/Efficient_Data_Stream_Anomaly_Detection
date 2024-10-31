import matplotlib.pyplot as plt

def visualize_real_time(i, value, stream, anomalies, window_size=50):
    """Updates the real-time plot with latest data and detected anomalies."""
    if not isinstance(i, int) or i < 0:
        raise ValueError("Index must be a non-negative integer.")
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a numeric type.")
    if not isinstance(anomalies, list):
        raise TypeError("Anomalies must be a list.")

    plt.clf()
    plt.title("Real-Time Data Stream and Anomaly Detection")
    plt.xlabel("Time")
    plt.ylabel("Value")
    
    start = max(0, i - window_size)
    x_values = list(range(start, i + 1))
    y_values = stream[start:i + 1]
    plt.plot(x_values, y_values, label="Data Stream", color="blue")
    
    anomaly_x = [a[0] for a in anomalies if a[1] is not None and a[0] >= start]
    anomaly_y = [a[1] for a in anomalies if a[1] is not None and a[0] >= start]
    plt.scatter(anomaly_x, anomaly_y, color="red", label="Anomalies")
    
    plt.legend()
    plt.pause(0.05)

