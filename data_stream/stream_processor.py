import time
import matplotlib.pyplot as plt
from visualization.real_time_plot import visualize_real_time

def simulate_data_stream(detector, stream, delay=0.1):
    """
    Simulates a real-time data stream by iterating over each value in the stream,
    applying an anomaly detector, and visualizing results in real-time.

    Parameters:
    -----------
    detector : object
        An anomaly detector object with a detect method that takes a data point
        as input and returns True if the point is an anomaly, otherwise False.
        
    stream : list or iterable
        The stream of data points to be processed and visualized in real-time.
        
    delay : float, optional (default=0.1)
        Time delay between processing each data point, simulating a real-time 
        data stream. Delay is specified in seconds.

    Returns:
    --------
    anomalies : list of tuples
        A list of tuples, where each tuple contains:
        - the index of the data point
        - the data point value if it was detected as an anomaly, or None otherwise.
    """
    
    anomalies = []

    for i, value in enumerate(stream):
        # Detect if the current data point is an anomaly
        is_anomaly = detector.detect(value)
        
        # Append the anomaly status to the list: include the index and value if an anomaly, else (index, None)
        anomalies.append((i, value) if is_anomaly else (i, None))
        
        # Update the real-time visualization with the current data point and detected anomalies
        visualize_real_time(i, value, stream, anomalies, window_size=100)
        
        time.sleep(delay)

    return anomalies
