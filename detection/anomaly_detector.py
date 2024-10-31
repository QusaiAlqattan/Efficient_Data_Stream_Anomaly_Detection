from scipy.stats import zscore
from collections import deque

class ZScoreAnomalyDetector:
    """Detects anomalies using Z-score."""
    def __init__(self, window_size=30, threshold=3):
        if not isinstance(window_size, int) or window_size <= 0:
            raise ValueError("window_size must be a positive integer.")
        if not isinstance(threshold, (int, float)):
            raise ValueError("threshold must be a numeric value.")

        self.window_size = window_size
        self.threshold = threshold
        self.data_window = deque(maxlen=window_size)
    
    def detect(self, value):
        """Detects if a value is an anomaly."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a numeric type.")
        
        self.data_window.append(value)
        
        if len(self.data_window) < self.window_size:
            return False
        
        z_scores = zscore(list(self.data_window))
        if abs(z_scores[-1]) > self.threshold:
            return True
        
        return False

