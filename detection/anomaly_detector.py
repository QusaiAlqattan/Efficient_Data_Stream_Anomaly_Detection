from scipy.stats import zscore
from collections import deque

class ZScoreAnomalyDetector:
    def __init__(self, window_size=30, threshold=3):
        self.window_size = window_size
        self.threshold = threshold
        self.data_window = deque(maxlen=window_size)
    
    def detect(self, value):
        # Add new data to the window
        self.data_window.append(value)
        
        # If there isn't enough data to calculate Z-score, return False
        if len(self.data_window) < self.window_size:
            return False
        
        # Calculate the Z-score of the last value
        z_scores = zscore(list(self.data_window))
        if abs(z_scores[-1]) > self.threshold:
            return True  # Flag as anomaly
        
        return False
