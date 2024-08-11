import base64
import os

base_path = '../Splitted-By-Protocol/'

# File paths
input_file_path = os.path.join(base_path, 'filtered_vmess_working.txt')
filtered_file_path = os.path.join(base_path, 'filtered_vmess.txt')

def read_file(file_path):
    """Read the content of a file."""
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, lines):
    """Write lines to a file."""
    with open(file_path, 'w') as file:
        file.writelines(lines)

def decode_vmess_link(encoded_link):
    """Decode a vmess link from base64."""
    try:
        decoded_bytes = base64.b64decode(encoded_link.replace('vmess://', ''))
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        print(f"Error decoding vmess link: {e}")
        return None

def is_vmess_link_working(link_data):
    """Placeholder function to check if the vmess link is working."""
    # Replace this function with actual testing logic
    # For example, you might use a library or network tool to verify the link
    return True

def process_vmess_links(input_file, output_file):
    """Process the vmess links and filter out non-working ones."""
    try:
        lines = read_file(input_file)
        working_links = []

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith('vmess://'):
                decoded_data = decode_vmess_link(line)
                if decoded_data and is_vmess_link_working(decoded_data):
                    working_links.append(line + '\n')
            else:
                # Keep lines that do not start with 'vmess://' as is
                working_links.append(line + '\n')

        write_file(output_file, working_links)
        print(f'Filtered links have been saved to {output_file}')
    except Exception as e:
        print(f"Error in process_vmess_links: {e}")

def overwrite_input_file_with_filtered(input_file, filtered_file):
    """Overwrite the input file with the content of the filtered file."""
    try:
        filtered_lines = read_file(filtered_file)
        write_file(input_file, filtered_lines)
        print(f'Content of {input_file} has been replaced with filtered links.')
    except Exception as e:
        print(f"Error in overwrite_input_file_with_filtered: {e}")

# Run the processing function
process_vmess_links(input_file_path, filtered_file_path)

# Overwrite the original file with the filtered content
overwrite_input_file_with_filtered(input_file_path, filtered_file_path)
