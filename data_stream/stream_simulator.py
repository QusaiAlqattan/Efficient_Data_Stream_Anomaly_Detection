import numpy as np
import random

def generate_data_stream(n_points=500):
    """Simulates a data stream with seasonality, noise, and occasional anomalies."""
    if not isinstance(n_points, int) or n_points <= 0:
        raise ValueError("n_points must be a positive integer.")
    
    data = []
    for i in range(n_points):
        # Seasonal component
        seasonal = 10 * np.sin(i / 50) + 50
        
        # Noise component
        noise = np.random.normal(0, 2)
        
        # Occasionally add an anomaly
        if random.random() < 0.01:
            anomaly = random.choice([50, -30])  # Choose a random extreme value
        else:
            anomaly = 0
            
        data.append(seasonal + noise + anomaly)
    
    return data
