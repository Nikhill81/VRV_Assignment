import re
from collections import defaultdict

# Set the path to your log file
log_file_path = '/Users/nikhil/Desktop/VRV_Assignment/03_Suspicious_Activity/server_logs.txt'

# Function to parse the log file and count failed login attempts per IP address
def parse_logs(file_path):
    ip_failed_attempts = defaultdict(int)
    
    # Open the log file and read it
    with open(file_path, 'r') as file:
        logs = file.readlines()
    
    print("Logs loaded:")
    print(logs)
    
    # Regular expression to match failed login attempts (401 errors)
    for log in logs:
        if 'POST /login' in log and '401' in log:
            ip_address = log.split(' ')[0]  # IP is the first part of the log
            ip_failed_attempts[ip_address] += 1  # Increment the failed attempt count for that IP
            print(f"Found failed attempt from: {ip_address}")
    
    return ip_failed_attempts

# Function to check for suspicious activity based on failed login attempts
def detect_suspicious_activity(ip_failed_attempts, threshold=3):
    suspicious_ips = {ip: attempts for ip, attempts in ip_failed_attempts.items() if attempts >= threshold}
    
    if suspicious_ips:
        print("\nSuspicious Activity Detected:")
        print("IP Address           Failed Login Attempts")
        print("========================================")
        for ip, attempts in suspicious_ips.items():
            print(f"{ip}        {attempts}")
    else:
        print("\nNo suspicious activity detected.")

# Main function to execute the script
def main():
    ip_failed_attempts = parse_logs(log_file_path)
    
    # Set the threshold to detect suspicious activity
    threshold = 3  # Lowered the threshold to 3 for easier detection
    detect_suspicious_activity(ip_failed_attempts, threshold)

if __name__ == '__main__':
    main()
