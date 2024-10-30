if __name__ == "__main__":
    # Generate a data stream
    stream = generate_data_stream()
    
    # Initialize the anomaly detector
    detector = ZScoreAnomalyDetector(window_size=30, threshold=3)
    
    # Set up real-time plotting
    plt.figure()
    
    # Run the data stream simulation
    simulate_data_stream(detector, stream)
    
    plt.show()
