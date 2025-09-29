import os
from PIL import Image

def set_transparency(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".png"):
            # Open the image
            img = Image.open(os.path.join(input_directory, filename)).convert("RGBA")
            
            # Get the image data
            datas = img.getdata()
            
            new_data = []
            for item in datas:
                # Change the alpha value to 50% (128/255)
                new_data.append((item[0], item[1], item[2], int(item[3] * 0.5)))
            
            # Update image data
            img.putdata(new_data)
            
            # Save the modified image to the output directory
            img.save(os.path.join(output_directory, filename))

# Define the input and output directories
input_directory = 'C:/Users/Florian/Desktop/Neuer Ordner (4)'
output_directory = 'C:/Users/Florian/AppData/Roaming/.minecraft/resourcepacks/Faithful 32x - 1.21/assets/minecraft/textures/particle'

# Set transparency of all PNGs in the input directory
set_transparency(input_directory, output_directory)
print("done")