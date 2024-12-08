import re
from collections import Counter

def analyze_log_file(log_file_path):

    """
    This function reads the log file, finds all the IP addresses, and counts how many times 
    each IP has made a request.

    Args:
        log_file_path (str): Path to the log file.

    Returns:
        list: A list of tuples with IP addresses and their request counts, sorted by the count (highest first).
    """

    try:
        with open(log_file_path, 'r') as log_file:
            log_lines = log_file.readlines()

        ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
        ip_addresses = []
        for line in log_lines:
            ip_addresses.extend(ip_pattern.findall(line))

        ip_counts = Counter(ip_addresses)
        return sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)

    except FileNotFoundError:
        print(f"Oops! Couldn't find the log file at '{log_file_path}'. Check the path and try again.")
        return []
    

def print_ip_stats(ip_counts):
    """
    Prints a formatted table of IP addresses and their occurrence counts.

    Args:
        ip_counts (list): A list of tuples containing IP addresses and their counts.
    """

    print("IP Address\tRequest Count")
    print("-" * 30)

    for ip, count in ip_counts:
        print(f"{ip}\t{count}")

if __name__ == "__main__":
    log_file_path = "access.log"  # Replace with your actual log file path

    ip_stats = analyze_log_file(log_file_path)

    if ip_stats:
        print_ip_stats(ip_stats)
    else:
        print("No IP data found in the log file.")