#!/usr/bin/python3
"""Log parsing"""

import sys
import signal


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the stats"""
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def signal_handler(sig, frame):
    """Signal handler"""
    print_stats()
    sys.exit(0)


# Set up signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin
try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        if len(data) < 7:
            continue

        # Get the data
        try:
            ip = data[0]
            date = data[3][1:]
            method = data[5][1:]
            path = data[6]
            protocol = data[7][:-1]
            status_code = int(data[8])
            size = int(data[9])
        except (ValueError, IndexError):
            continue

        # Ensure the format matches
        if (method == 'GET' and path ==
                '/projects/260' and
                protocol == 'HTTP/1.1'):
            total_size += size
            if status_code in status_codes:
                status_codes[status_code] += 1
            line

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
