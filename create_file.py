import os

# Specify the file path
file_path = 'my_dir/filename.txt'
directory = os.path.dirname(file_path)

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write some content to the file
    file.write('Hello, this is a test file.\n')
    file.write('Writing multiple lines is easy with Python.')

# The file is automatically closed when the 'with' block ends
