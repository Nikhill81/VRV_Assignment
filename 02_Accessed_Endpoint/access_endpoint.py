import os
import csv
from collections import Counter

def get_most_least_accessed_endpoint(log_file):
    """
    Reads the log file and calculates the most and least accessed endpoints.

    Args:
    log_file (str): Path to the log file.

    Returns:
    tuple: Most and least accessed endpoint data.
    """
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()

        # Extract the accessed endpoints from the log lines
        endpoints = [line.split()[6] for line in lines if len(line.split()) > 6]

        # Count the frequency of each endpoint
        endpoint_counts = Counter(endpoints)

        # Find the most and least accessed endpoints
        most_accessed = endpoint_counts.most_common(1)[0]  # (endpoint, count)
        least_accessed = endpoint_counts.most_common()[-1]  # (endpoint, count)

        return most_accessed, least_accessed

    except FileNotFoundError:
        print(f"Error: The file {log_file} was not found.")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None


def save_to_csv(data, output_file):
    """
    Saves the most and least accessed endpoint data to a CSV file.

    Args:
    data (tuple): Contains the endpoint data (endpoint, count).
    output_file (str): Path to the output CSV file.
    """
    if data:
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Endpoint', 'Access Count'])
            writer.writerow(data)


def main():
    """
    Main function to handle the log analysis and output.
    """
    # Get the current script directory dynamically
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Define the relative paths for the log file and output files
    log_file = os.path.join(current_directory, 'test_accessed_endpoints.txt')
    output_file_most = os.path.join(current_directory, 'most_accessed_endpoint.csv')
    output_file_least = os.path.join(current_directory, 'least_accessed_endpoint.csv')

    print(f"Looking for log file at: {log_file}")

    # Get the most and least accessed endpoints
    most_accessed, least_accessed = get_most_least_accessed_endpoint(log_file)

    if most_accessed and least_accessed:
        print(f"Most Frequently Accessed Endpoint: {most_accessed[0]} (Accessed {most_accessed[1]} times)")
        print(f"Least Frequently Accessed Endpoint: {least_accessed[0]} (Accessed {least_accessed[1]} times)")

        # Save the results to CSV files
        save_to_csv(most_accessed, output_file_most)
        save_to_csv(least_accessed, output_file_least)

        print(f"Most accessed endpoint saved to: {output_file_most}")
        print(f"Least accessed endpoint saved to: {output_file_least}")
    else:
        print("No data found in the log file. Exiting.")


if __name__ == '__main__':
    main()
