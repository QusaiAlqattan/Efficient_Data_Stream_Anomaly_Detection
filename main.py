# Import necessary modules
from data_stream.stream_simulator import generate_data_stream
from detection.anomaly_detector import ZScoreAnomalyDetector
from data_stream.stream_processor import simulate_data_stream  # Ensure this function is defined in stream_processor
import matplotlib.pyplot as plt
from utils.logger import setup_logger, log_error

setup_logger()

if __name__ == "__main__":
    # Generate a data stream
    try:
        stream = generate_data_stream()
    except Exception as e:
        log_error(f"Error generating data stream: {e}")
    
    # Initialize the anomaly detector
    detector = ZScoreAnomalyDetector(window_size=30, threshold=3.3)
    
    # Set up real-time plotting
    plt.figure()
    
    # Run the data stream simulation
    simulate_data_stream(detector, stream)
    
    plt.show()
