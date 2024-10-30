import matplotlib.pyplot as plt

def visualize_real_time(i, value, anomalies, window_size=50):
    """Updates the real-time plot with the latest data point and anomalies."""
    plt.clf()  # Clear previous plot
    plt.title("Real-Time Data Stream and Anomaly Detection")
    plt.xlabel("Time")
    plt.ylabel("Value")
    
    # Plot data in the current window
    start = max(0, i - window_size)
    x_values = list(range(start, i + 1))
    y_values = stream[start:i + 1]
    plt.plot(x_values, y_values, label="Data Stream", color="blue")
    
    # Highlight anomalies in red
    anomaly_x = [a[0] for a in anomalies if a[1] is not None and a[0] >= start]
    anomaly_y = [a[1] for a in anomalies if a[1] is not None and a[0] >= start]
    plt.scatter(anomaly_x, anomaly_y, color="red", label="Anomalies")
    
    plt.legend()
    plt.pause(0.05)  # Small pause to update the plot
