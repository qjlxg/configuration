import json
import base64
import requests
import os
import queue
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# File paths
base_path = '../'

def load_vmess_data(file_path):
    """Load VMess data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading VMess data from file {file_path}: {e}")
        return []

def is_valid_vmess(vmess_data):
    """Check if a VMess link is valid by making an HTTP request."""
    # Remove any leading or trailing whitespace from port
    port = vmess_data.get('port', '').strip()
    
    if not port:
        print(f"Missing or invalid port in VMess data: {vmess_data}")
        return False
    
    # Construct the URL for testing the VMess link
    url = f"http://{vmess_data.get('add', '')}:{port}/"
    
    # Print the URL being tested for debugging
    print(f"Testing URL: {url}")
    
    try:
        # Send a request to the URL
        response = requests.get(url, timeout=30)
        # Check if the response is successful (status code 200)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return False

def encode_base64(vmess_data):
    """Encode VMess data in Base64."""
    try:
        # Convert the dictionary to a JSON string
        json_str = json.dumps(vmess_data, separators=(',', ':'))
        # Encode the JSON string in Base64
        return base64.b64encode(json_str.encode()).decode()
    except (TypeError, ValueError) as e:
        print(f"Error encoding VMess data to Base64: {e}")
        return None

def process_chunk(chunk, result_queue):
    """Process a chunk of VMess data and put valid results into a queue."""
    print(f"Processing chunk with {len(chunk)} items")
    for vmess_data in chunk:
        try:
            if is_valid_vmess(vmess_data):
                encoded_data = encode_base64(vmess_data)
                if encoded_data:
                    result_queue.put(f"vmess://{encoded_data}")
                else:
                    print(f"Failed to encode VMess data: {vmess_data}")
            else:
                print("Invalid VMess link:", vmess_data)
        except Exception as e:
            print(f"Error processing VMess data {vmess_data}: {e}")

def write_results(result_queue, file_path):
    """Write results from the queue to the output file."""
    print(f"File writer thread started for {file_path}")
    try:
        with open(file_path, 'a') as file:
            while True:
                result = result_queue.get()
                if result is None:
                    break
                try:
                    file.write(result + '\n')
                    print(f"Written result to file: {result}")
                except IOError as e:
                    print(f"Error writing result to file: {e}")
    except IOError as e:
        print(f"Error opening file {file_path} for writing: {e}")

def main():
    input_file = os.path.join(base_path, 'vmess_updated.json')
    output_file = os.path.join(base_path, 'vmess_working.txt')
    
    # Ensure output file is empty before starting
    try:
        open(output_file, 'w').close()
    except IOError as e:
        print(f"Error opening file {output_file} for writing: {e}")
        return

    vmess_list = load_vmess_data(input_file)
    
    # Check if the input file is loaded correctly
    if not vmess_list:
        print("No VMess data found in the input file.")
        return

    # Create a thread-safe queue for results
    result_queue = queue.Queue()

    # Define the number of threads
    num_threads = 500

    # Split the list into chunks for each thread
    chunk_size = max(1, len(vmess_list) // num_threads)
    chunks = [vmess_list[i:i + chunk_size] for i in range(0, len(vmess_list), chunk_size)]
    
    # Start the file writer thread
    file_writer_thread = threading.Thread(target=write_results, args=(result_queue, output_file))
    file_writer_thread.start()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Submit each chunk to a separate thread
        futures = [executor.submit(process_chunk, chunk, result_queue) for chunk in chunks]
        
        # Wait for all threads to complete
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Thread encountered an error: {e}")

    # Signal the file writer thread to stop
    result_queue.put(None)
    file_writer_thread.join()
    print("All threads have completed and file writing is done.")

if __name__ == "__main__":
    main()
