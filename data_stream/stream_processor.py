import time
import matplotlib.pyplot as plt
from visualization.real_time_plot import visualize_real_time

def simulate_data_stream(detector, stream, delay=0.1):
    """Simulates a real-time data stream, applying the anomaly detector to each value."""
    anomalies = []
    for i, value in enumerate(stream):
        is_anomaly = detector.detect(value)
        anomalies.append((i, value) if is_anomaly else (i, None))
        
        # Pass the stream variable to visualize_real_time
        visualize_real_time(i, value, stream, anomalies, window_size=50)
        
        time.sleep(delay)
    return anomalies
