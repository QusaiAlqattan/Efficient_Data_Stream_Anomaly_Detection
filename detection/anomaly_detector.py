from scipy.stats import zscore
from collections import deque

class ZScoreAnomalyDetector:
    """
    Anomaly detector using a rolling Z-score method. Maintains a fixed-size window 
    of recent values, calculating Z-scores to detect anomalies based on deviation 
    from the mean of the window.
    """
    def __init__(self, window_size=30, threshold=3):
        """
        Initializes the Z-score anomaly detector with specified window size and threshold.

        Parameters:
        -----------
        window_size : int, optional (default=30)
            The number of recent data points to retain in the rolling window for 
            Z-score calculations. Must be a positive integer.
            
        threshold : float, optional (default=3)
            The Z-score threshold above which a data point is considered an anomaly.
            Must be a numeric value.
        """

        if not isinstance(window_size, int) or window_size <= 0:
            raise ValueError("window_size must be a positive integer.")
        if not isinstance(threshold, (int, float)):
            raise ValueError("threshold must be a numeric value.")

        self.window_size = window_size
        self.threshold = threshold

        # Initialize a deque to store a fixed-size rolling window of recent values
        self.data_window = deque(maxlen=window_size)
    
    def detect(self, value):
        """
        Detects if a given value is an anomaly based on the Z-score in the current window.

        Parameters:
        -----------
        value : float or int
            The new data point to be tested for anomalies.

        Returns:
        --------
        bool
            True if the data point is an anomaly, False otherwise.
        """

        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a numeric type.")
        
        self.data_window.append(value)
        
        # Check if the window has enough data points for meaningful Z-score calculation
        if len(self.data_window) < self.window_size:
            return False
        
        # Compute Z-scores for all values in the window
        z_scores = zscore(list(self.data_window))
        
        if abs(z_scores[-1]) > self.threshold:
            # Remove the anomaly from the window to prevent shifting the mean suddenly
            self.data_window.pop()
            return True
        
        return False
