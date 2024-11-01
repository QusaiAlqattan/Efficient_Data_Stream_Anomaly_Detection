import numpy as np
import random

def generate_data_stream(n_points=300):
    """Simulates a data stream with seasonality, noise, and different types of anomalies."""
    if not isinstance(n_points, int) or n_points <= 0:
        raise ValueError("n_points must be a positive integer.")
    
    data = []
    for i in range(n_points):
        # Seasonal component
        seasonal = 10 * np.sin(i / 50) + 50
        
        # Noise component
        noise = np.random.normal(0, 2)
        
        # Initialize anomaly to 0 (no anomaly by default)
        anomaly = 0
        
        # Define anomaly probabilities for different types
        global_outlier_prob = 0.01  # Global outlier probability
        contextual_outlier_prob = 0.02  # Contextual outlier probability
        collective_outlier_prob = 0.005  # Probability of starting a collective anomaly

        # Global Outliers: large, rare anomalies
        if random.random() < global_outlier_prob:
            anomaly = random.choice([80, -50])  # Very high or very low outliers
        
        # Contextual Outliers: anomalies based on context (e.g., unusually high or low for the season)
        elif random.random() < contextual_outlier_prob:
            if seasonal > 50:  # During high seasonality, add a negative contextual anomaly
                anomaly = -20
            else:  # During low seasonality, add a positive contextual anomaly
                anomaly = 20

        # Collective Outliers: consecutive anomalies
        elif random.random() < collective_outlier_prob:
            # Start a series of 5-10 anomalous points
            anomaly = [random.choice([15, -15]) for _ in range(random.randint(5, 10))]
        
        # If we generated a series of anomalies (collective), add them to data
        if isinstance(anomaly, list):
            # Add collective anomalies as consecutive points in the data
            data.extend([seasonal + noise + a for a in anomaly])
            # Skip the next points since they are already populated
            i += len(anomaly) - 1  # Move the loop index forward to skip over the collective anomaly
        else:
            # Single-point anomaly (either global or contextual)
            data.append(seasonal + noise + anomaly)
    
    # Ensure we don't exceed n_points if collective anomalies push us over
    return data[:n_points]
