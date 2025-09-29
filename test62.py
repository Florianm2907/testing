import hashlib

# Function to hash a line of text with SHA-256 and salt
def hash_line(line, salt):
    # Combine the line and salt
    data = salt.encode('utf-8') + line.encode('utf-8')
    
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the combined data
    sha256.update(data)
    
    # Get the hexadecimal representation of the hash
    hashed_value = sha256.hexdigest()
    
    return hashed_value 

# Input file name and salt
input_file = "F:/FESTPLATTE H/test1/max.txt"  # Replace with your input file
salt = "3NL/usjb4vEg"         # Replace with your salt

# Output file name
output = []

# Read lines from the input file, hash them, and save to the output file
hashed_lines = []
with open(input_file, 'r') as infile:
    for line in infile:
        line = line.strip()
        hashed_line = hash_line(line, salt)
        hashed_lines.append(hashed_line)
given_hash = "47fde76c898053a9db963df844bb936c26ab54867663f4d1505858d6c346eacc"
# if "47fde76c898053a9db963df844bb936c26ab54867663f4d1505858d6c346eacc" in output:
#     print
        
found = False
for i, hashed_line in enumerate(hashed_lines):
    # print(hashed_line)
    if hashed_line == given_hash:
        print(f"Matching line found at index {i/2}: {line}")
        found = True

if not found:
    print(f"No matching line found for the given hash.")

# print(f"Hashed lines from {input_file} with SHA-256 and salt '{salt}")
print(hash_line("xam_862001", salt))