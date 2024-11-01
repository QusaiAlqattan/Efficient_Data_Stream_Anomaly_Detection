import numpy as np
import random

def generate_data_stream(n_points=300):
    """
    Generates a simulated data stream with seasonality, noise, and different types
    of anomalies (global, contextual, and collective).

    Parameters:
    -----------
    n_points : int, optional (default=300)
        Number of data points to generate in the simulated data stream.

    Returns:
    --------
    data : list of floats
        A list of generated data points, where each point may include seasonal patterns,
        noise, and occasional anomalies.
    """

    if not isinstance(n_points, int) or n_points <= 0:
        raise ValueError("n_points must be a positive integer.")
    
    data = []
    
    for i in range(n_points):
        # Seasonal component: sine wave to seasonality
        seasonal = 10 * np.sin(i / 50) + 50
        
        # Noise component: small random fluctuation around each seasonal point
        noise = np.random.normal(0, 2)
        
        # No anomaly by default
        anomaly = 0
        
        global_outlier_prob = 0.01  # Probability of a global outlier
        contextual_outlier_prob = 0.02  # Probability of a contextual outlier
        collective_outlier_prob = 0.005  # Probability of starting a collective anomaly

        # Generate Global Outliers
        if random.random() < global_outlier_prob:
            anomaly = random.choice([80, -50])
        
        # Generate Contextual Outliers
        elif random.random() < contextual_outlier_prob:
            # If seasonal component is high, add a negative contextual anomaly; if low, add positive
            if seasonal > 50:
                anomaly = -20
            else:
                anomaly = 20

        # Generate Collective Outliers
        elif random.random() < collective_outlier_prob:
            # Start a series of 5-10 consecutive anomalies with moderate values
            anomaly = [random.choice([15, -15]) for _ in range(random.randint(5, 10))]
        
        # Handle collective anomalies as a sequence of consecutive points
        if isinstance(anomaly, list):
            # Add each anomaly in the sequence to the data stream with seasonal and noise components
            data.extend([seasonal + noise + a for a in anomaly])
            # Adjust loop counter to skip over the added sequence points in the next iterations
            i += len(anomaly) - 1
        else:
            # Add single-point anomaly (global or contextual) to the data stream
            data.append(seasonal + noise + anomaly)
    
    # Ensure the final data stream length does not exceed n_points in case of collective anomalies
    return data[:n_points]
