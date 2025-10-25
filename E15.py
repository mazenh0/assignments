def time_as_seconds(time: str) -> int:
    """Convert time in hh:mm:ss format to seconds since midnight."""
    # Split the time string into hours, minutes, and seconds using ':'
    split_time = time.split(':')
    # Convert the hours, minutes, and seconds into integers
    hours = int(split_time[0])
    minutes = int(split_time[1])
    seconds = int(split_time[2])
    # Return the total time in seconds
    # Formula: (hours * 3600) + (minutes * 60) + seconds
    return (hours * 60 * 60) + (minutes * 60) + seconds
# Main function to process the game log file
def process_log_file(filename: str):
    # Initialize the total points scored to 0
    total_points = 0  
    # Initialize start time and end time to 0
    start_time = 0
    end_time = 0
    with open(filename, 'r') as file:
        # Read all lines from the file into a list
        lines = file.readlines()
        # Loop through each line in the file using its index and content
        for i, line in enumerate(lines):
            # Strip leading/trailing whitespace and split the line into words
            parts = line.strip().split()
            # Extract the time (first word of the line)
            time = parts[0]
            # If it's the first line, set the start time
            if i == 0:  
                start_time = time_as_seconds(time)
            # Update the end time every iteration to get the last line's time
            end_time = time_as_seconds(time)
            # Check if the line contains the word "score"
            if "score" in line:
                # Extract the points scored: second to last word in the line
                points = int(parts[-2])
                # Add the points to the total points counter
                total_points += points
    duration = end_time - start_time
    # Print the total points scored
    print("Total points scored:", total_points)
    # Print the game duration in seconds
    print("Game duration in seconds:", duration)
process_log_file('log.txt')
