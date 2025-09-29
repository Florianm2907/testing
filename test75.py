import os
from collections import defaultdict

def get_filenames(directories):
    filenames = defaultdict(list)
    system_file_extensions = ['.dll', '.dat', '.sys', '.log', '.pak', '.cas', 'vpk', '.db', '.jar']  # Define system file extensions to filter out
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                # Check if the file extension is in the list of system file extensions
                if not any(full_path.lower().endswith(ext) for ext in system_file_extensions) and not "data" in full_path.lower():
                    filenames[file].append(full_path)
    return filenames

# def find_duplicates(filenames, min_size):
#     duplicates = defaultdict(list)
#     for filename, paths in filenames.items():
#         if len(paths) > 1:
#             file_sizes = {path: os.path.getsize(path) for path in paths}
#             unique_sizes = set(file_sizes.values())
#             if len(unique_sizes) == 1:  # Check if all file sizes are the same
#                 for path in paths:
#                     if os.path.getsize(path) > min_size * 1024 * 1024:  # Check if file size is greater than 10MB
#                         duplicates[filename].append(path)
#                 if duplicates[filename]:  # If duplicate paths exist
#                     duplicates[filename] = len(duplicates[filename])  # Count occurrences
#                 else:
#                     del duplicates[filename]  # Remove filename if no duplicates larger than 10MB
#     return duplicates

def find_duplicates(filenames, min_size):
    duplicates = {}
    for filename, paths in filenames.items():
        if len(paths) > 1:
            # Get the size of the first file in the list
            first_size = os.path.getsize(paths[0])
            # Check if all files have the same size
            if all(os.path.getsize(path) == first_size for path in paths):
                # Check if the size is greater than min_size
                if first_size > min_size * 1024 * 1024:
                    # Add the filename to duplicates dictionary
                    duplicates[filename] = paths
    return duplicates

if __name__ == "__main__":
    # Specify the directory to start searching from
    directories = ['C:/', 'E:/', 'F:/', 'Z:/']
    min_size = 20
    all_duplicates = []
    # Get filenames
    print("processing files")
    filenames = get_filenames(directories)
    print("processing duplicates")
    duplicates = find_duplicates(filenames, min_size)

    output_file = "duplicate_files.txt"
    # with open(output_file, "w", encoding="utf-8") as f:
    #     if duplicates:
    #         print("writing")
    #         f.write("Duplicate filenames larger than 20mb found:\n")
    #         for filename, paths_or_count in duplicates.items():
    #             f.write(f"Filename: {filename}\n")
    #             f.write("Locations:\n")
    #             for path in paths_or_count:
    #                 f.write(f"{path}\n")
    #             # Check if paths_or_count is an integer (count of occurrences)
    #             if isinstance(paths_or_count, int):
    #                 f.write(f"Number of occurrences: {paths_or_count}\n")
    #             else:
    #                 for path in paths_or_count:
    #                     f.write(f"{path}\n")
    #             f.write("\n")
    #     else:
    #         f.write(f"No duplicate filenames larger than {min_size} found.\n")
    with open(output_file, "w", encoding="utf-8") as f:
        if duplicates:
            f.write(f"Duplicate filenames larger than {min_size}MB found:\n")
            for filename, paths in duplicates.items():
                f.write(f"Filename: {filename}\n")
                f.write("Locations:\n")
                for path in paths:
                    f.write(f"{path}\n")
                f.write("\n")
        else:
            f.write(f"No duplicate filenames larger than {min_size}MB found.\n")

    print(f"Output written to {output_file}")

    # # Display filenames
    # for filename in filenames:
    #     print(filename)