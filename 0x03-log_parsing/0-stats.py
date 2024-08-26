#!/usr/bin/python3
import sys
import signal
import re


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

log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
)

def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))

            total_file_size += file_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    pass

finally:
    print_stats()