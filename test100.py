import os
from PIL import Image
import pillow_avif
# Set the directory path
directory = "C:/nginx-html/media"

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):  # Check if it's an image
        file_path = os.path.join(directory, filename)
        
        try:
            # Open the image
            with Image.open(file_path) as img:
                # Reduce resolution by half
                if img.width > 1000: new_size = (img.width // 2, img.height // 2)
                img = img.resize(new_size, Image.LANCZOS)
                
                # Create the new file name
                new_filename = f"{os.path.splitext(filename)[0]}_1.avif"
                new_file_path = os.path.join(directory, new_filename)
                
                # Save the image in AVIF format with high quality
                img.save(new_file_path, format="AVIF", quality=70)

                print(f"Compressed and saved {new_filename}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")
