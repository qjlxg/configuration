import os
import base64

def read_file(file_path):
    """Read the content of a file."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def create_subscription_link(input_path, output_path):
    """Create a base64-encoded subscription link."""
    try:
        vmess_links = read_file(input_path)
        combined_links = vmess_links.strip()
        base64_data = base64.b64encode(combined_links.encode('utf-8')).decode('utf-8')
        subscription_link = f"{base64_data}"
        write_file(output_path, subscription_link)
        print(f'Subscription link has been saved to {output_path}')
    except Exception as e:
        print(f"Error in create_subscription_link: {e}")

# File paths
base_path = '../Splitted-By-Protocol/'
file_paths = {
    'subscription': os.path.join(base_path, 'filtered_vmess_working.txt'),
    'final_subscription': os.path.join(base_path, 'vmess_subscription_link.txt')
}

# Run the processing function
create_subscription_link(file_paths['subscription'], file_paths['final_subscription'])
