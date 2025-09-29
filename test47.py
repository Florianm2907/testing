import os

# Function to read and output the content of text files in a folder
def read_text_files_in_folder(folder_path):
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"The folder '{folder_path}' does not exist.")
            return

        # List all files in the folder
        file_list = os.listdir(folder_path)

        # Iterate through the files
        for file_name in file_list:
            # Check if the file is a text file (ends with '.txt')
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder_path, file_name)

                # Open and read the file
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Output the content
                print({content})

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing the text files: ")
    read_text_files_in_folder(folder_path)
