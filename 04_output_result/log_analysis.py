import csv
import os
from collections import defaultdict

def analyze_logs(log_file_path):
    """
    Analyzes the given log file to:
    - Track the number of requests per IP
    - Identify the most accessed endpoints
    - Track suspicious failed login attempts
    """
    # Initialize data structures
    ip_requests = defaultdict(int)
    endpoint_counts = defaultdict(int)
    failed_logins = defaultdict(int)

    # Check if the log file exists
    if not os.path.isfile(log_file_path):
        print(f"Error: The log file {log_file_path} was not found.")
        return


    # Open the log file and process each line
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(" ")
            
            # Check if the line has enough data (IP, endpoint, status)
            if len(parts) < 3:
                continue
            
            ip_address, endpoint, status = parts[0], parts[1], parts[2]

            # Count requests per IP
            ip_requests[ip_address] += 1
            
            # Count accesses to each endpoint
            endpoint_counts[endpoint] += 1
            
            # Track failed login attempts
            if status == "failed":
                failed_logins[ip_address] += 1

    # Output the results to the terminal
    print("Log Analysis Complete.")
    print("\nRequests per IP:")
    print("IP Address           Request Count")
    for ip, count in ip_requests.items():
        print(f"{ip:<20} {count}")
    
    print("\nMost Accessed Endpoint:")
    print("Endpoint                      Access Count")
    for endpoint, count in endpoint_counts.items():
        print(f"{endpoint:<30} {count}")
    
    print("\nSuspicious Activity (Failed Logins):")
    print("IP Address           Failed Login Count")
    for ip, count in failed_logins.items():
        print(f"{ip:<20} {count}")
    
    # Save the results to a CSV file
    with open('log_analysis_results.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write Requests per IP
        csv_writer.writerow(["Requests per IP"])
        csv_writer.writerow(["IP Address", "Request Count"])
        for ip, count in ip_requests.items():
            csv_writer.writerow([ip, count])
        
        # Write Most Accessed Endpoint
        csv_writer.writerow([])
        csv_writer.writerow(["Most Accessed Endpoint"])
        csv_writer.writerow(["Endpoint", "Access Count"])
        for endpoint, count in endpoint_counts.items():
            csv_writer.writerow([endpoint, count])
        
        # Write Suspicious Activity
        csv_writer.writerow([])
        csv_writer.writerow(["Suspicious Activity"])
        csv_writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in failed_logins.items():
            csv_writer.writerow([ip, count])

    print("\nResults have been saved to 'log_analysis_results.csv'.")

# Main entry point of the script
if __name__ == "__main__":
    print("Log Analysis Script Starting...")
    log_file_path = '/path/to/your/logfile/access_log.txt'  # Replace with your actual log file path
    analyze_logs(log_file_path)
