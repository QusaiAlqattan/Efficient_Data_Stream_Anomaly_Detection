# Import necessary modules
from data_stream.stream_simulator import generate_data_stream
from detection.anomaly_detector import ZScoreAnomalyDetector
from data_stream.stream_processor import simulate_data_stream  # Ensure this function is defined in stream_processor
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Generate a data stream
    stream = generate_data_stream()
    
    # Initialize the anomaly detector
    detector = ZScoreAnomalyDetector(window_size=30, threshold=4)
    
    # Set up real-time plotting
    plt.figure()
    
    # Run the data stream simulation
    simulate_data_stream(detector, stream)
    
    plt.show()
