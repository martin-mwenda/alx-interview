#!/usr/bin/python3
"""Reads stdin line by line and computes metrics.

For every 10 lines read or upon keyboard interruption (CTRL+C),
it outputs:
- Total file size: Sum of all file sizes encountered.
- Number of occurrences of each HTTP status code from a predefined list.
"""

import sys

# Initialize total file size and line counter
total_size = 0
counter = 0

# Predefined list of status codes of interest
codes = ['200', '301', '400', '401', '403', '404', '405', '500']

# Dictionary to count occurrences of each status code
dict_counter = {code: 0 for code in codes}

try:
    # Read each line from stdin
    for line in sys.stdin:
        # Split the line by whitespace
        line_list = line.split(" ")

        # Check if line has enough parts (skip malformed lines)
        if len(line_list) > 2:
            # Extract status code and file size from the end of the line
            code = line_list[-2]
            size = line_list[-1]

            # Update status code count if it’s in our list
            if code in codes:
                dict_counter[code] += 1

            # Add file size to total (cast to int)
            total_size += int(size)
            counter += 1

        # Print metrics every 10 lines
        if counter == 10:
            print("File size: {:d}".format(total_size))
            for k, v in sorted(dict_counter.items()):
                if v != 0:
                    print("{}: {:d}".format(k, v))
            counter = 0

except Exception:
    # Ignore exceptions silently (can be expanded if needed for debugging)
    pass

finally:
    # Print final metrics after all input has been processed
    print("File size: {}".format(total_size))
    for k, v in sorted(dict_counter.items()):
        if v != 0:
            print("{}: {}".format(k, v))
