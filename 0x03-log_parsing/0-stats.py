#!/usr/bin/python3
"""
A script that reads from standard input (stdin) line by line,
processes log entries, computes metrics based on specific log formats,
and handles keyboard interruptions gracefully.

The script:
- Reads from stdin line by line.
- Aggregates data such as total file size and counts of
  specific HTTP status codes.
- Prints statistics after every 10 lines or when interrupted
  by a keyboard signal (Ctrl+C).
"""

import sys
import signal

# Initialize total file size and status code counts
total_file_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

def print_stats():
    """
    Prints the current statistics:
    - Total file size of all processed log entries.
    - Count of occurrences for each HTTP status code.
    
    Only status codes with a count greater than 0 are printed.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """
    Signal handler function to handle keyboard interruption (Ctrl+C).
    
    When a SIGINT (Ctrl+C) signal is received:
    - Prints the current statistics.
    - Exits the program gracefully with status code 0.
    
    Parameters:
    - sig (int): The signal number.
    - frame (frame object): The current stack frame.
    """
    print_stats()
    sys.exit(0)

# Set up the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Initialize line counter
line_count = 0

try:
    # Read from standard input (stdin) line by line
    for line in sys.stdin:
        line = line.strip()  # Remove leading/trailing whitespace
        line_parts = line.split()  # Split line into parts

        if len(line_parts) >= 2:  # Ensure there are enough parts to parse
            try:
                # Extract status code and file size
                status_code = line_parts[-2]
                file_size = int(line_parts[-1])

                # Update total file size
                total_file_size += file_size

                # Update status code counts if the status code is valid
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

            except (IndexError, ValueError):
                # Handle any error in parsing
                pass

        line_count += 1  # Increment line count

        # Print stats after every 10 lines
        if line_count == 10:
            print_stats()
            line_count = 0  # Reset line count after printing

except KeyboardInterrupt:
    # Handle keyboard interruption gracefully
    print_stats()
    raise

finally:
    # Print final stats before exiting
    print_stats()
