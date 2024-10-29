0x03. Log Parsing

script that reads stdin line by line and computes metrics
The script uses regular expressions to match the specified log format, tracks
the total file size, and counts occurrences of each relevant status code.
Every 10 lines or upon a keyboard interrupt (e.g., CTRL + C),
it prints the total file size and the counts of each status code
