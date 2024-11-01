import matplotlib.pyplot as plt

def visualize_real_time(i, value, stream, anomalies, window_size=50):
    """
    Updates the real-time plot with the latest data and detected anomalies.

    Parameters:
    -----------
    i : int
        The current index in the data stream, indicating the time step of the value.
        
    value : float or int
        The latest data point value to be plotted.
        
    stream : list
        The complete data stream of values.
        
    anomalies : list
        A list of detected anomalies, where each anomaly is represented as a tuple
        (index, value), with None for values that are not anomalies.
        
    window_size : int, optional (default=50)
        The number of most recent data points to display in the plot. 
    """

    if not isinstance(i, int) or i < 0:
        raise ValueError("Index must be a non-negative integer.")
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a numeric type.")
    if not isinstance(anomalies, list):
        raise TypeError("Anomalies must be a list.")

    # Clear the current figure for real-time updates
    plt.clf()
    
    plt.title("Real-Time Data Stream and Anomaly Detection")
    plt.xlabel("Time")
    plt.ylabel("Value")
    
    # Calculate the starting index for the window of data points to display
    start = max(0, i - window_size)
    
    x_values = list(range(start, i + 1))

    y_values = stream[start:i + 1]
    
    plt.plot(x_values, y_values, label="Data Stream", color="blue")
    
    # Extract the x and y coordinates of detected anomalies for plotting
    anomaly_x = [a[0] for a in anomalies if a[1] is not None and a[0] >= start]
    anomaly_y = [a[1] for a in anomalies if a[1] is not None and a[0] >= start]
    
    # Plot the anomalies as red points on the graph
    plt.scatter(anomaly_x, anomaly_y, color="red", label="Anomalies")
    
    plt.legend()
    
    # Pause briefly to allow the plot to update in real-time
    plt.pause(0.05)
