import os

# File paths
base_path = '../Splitted-By-Protocol/'

def remove_duplicates(input_file, output_file):
    # Read all lines from the input file and remove duplicates
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Remove duplicate lines while preserving the order
    unique_lines = list(dict.fromkeys(lines))

    # Write the unique lines to the output file
    with open(output_file, 'w') as file:
        file.writelines(unique_lines)

# Define input and output file paths
input_file = os.path.join(base_path, 'vmess_working.txt')
output_file = os.path.join(base_path, 'filtered_vmess_working.txt')

# Call the function to remove duplicates
remove_duplicates(input_file, output_file)
