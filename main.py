# Import necessary modules for data generation, anomaly detection, simulation, plotting, and logging
from data_stream.stream_simulator import generate_data_stream
from detection.anomaly_detector import ZScoreAnomalyDetector
from data_stream.stream_processor import simulate_data_stream  # Ensure this function is defined in stream_processor
import matplotlib.pyplot as plt
from utils.logger import setup_logger, log_error

setup_logger()

if __name__ == "__main__":
    """
    Main execution block for generating a data stream, initializing the anomaly detector,
    and simulating the real-time processing of the data stream with anomaly detection.
    """

    # Generate a data stream with simulated values
    try:
        stream = generate_data_stream()
    except Exception as e:
        log_error(f"Error generating data stream: {e}")
    
    # Initialize the Z-score anomaly detector with specified parameters
    detector = ZScoreAnomalyDetector(window_size=30, threshold=3.3)
    
    # Set up a new figure for real-time plotting
    plt.figure()
    
    # Run the simulation of processing the data stream for anomaly detection
    simulate_data_stream(detector, stream)
    
    # Display the plot with the real-time data and detected anomalies
    plt.show()
