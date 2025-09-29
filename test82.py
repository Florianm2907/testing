import numpy as np
from PIL import Image
from stl import mesh

def image_to_height_map(image_path, max_height=10.0, resolution_scale=1.0):
    # Load image and convert to grayscale
    image = Image.open(image_path).convert('L')  # 'L' mode converts to grayscale
    
    # Resize image based on the resolution scale
    if resolution_scale != 1.0:
        new_size = (int(image.width * resolution_scale), int(image.height * resolution_scale))
        image = image.resize(new_size, Image.LANCZOS)
    
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Normalize pixel values to range [0, 1]
    normalized_array = image_array / 255.0
    
    # Invert brightness to height (0 = max_height, 1 = 0 height)
    height_map = max_height * (1 - normalized_array)
    
    return height_map

def height_map_to_stl(height_map, output_path, scale=1.0):
    rows, cols = height_map.shape
    vertices = []
    faces = []
    vertex_dict = {}
    
    def get_vertex_index(x, y, z):
        key = (x, y, z)
        if key not in vertex_dict:
            vertex_dict[key] = len(vertices)
            vertices.append([x * scale, y * scale, z])
        return vertex_dict[key]
    
    # Create top surface vertices and faces
    for i in range(rows):
        for j in range(cols):
            get_vertex_index(i, j, height_map[i, j])
    
    for i in range(rows - 1):
        for j in range(cols - 1):
            v1 = get_vertex_index(i, j, height_map[i, j])
            v2 = get_vertex_index(i + 1, j, height_map[i + 1, j])
            v3 = get_vertex_index(i + 1, j + 1, height_map[i + 1, j + 1])
            v4 = get_vertex_index(i, j + 1, height_map[i, j + 1])
            faces.append([v1, v2, v3])
            faces.append([v1, v3, v4])
    
    # Create bottom surface vertices and faces (z = 0)
    for i in range(rows):
        for j in range(cols):
            get_vertex_index(i, j, 0)
    
    for i in range(rows - 1):
        for j in range(cols - 1):
            v1 = get_vertex_index(i, j, 0)
            v2 = get_vertex_index(i + 1, j, 0)
            v3 = get_vertex_index(i + 1, j + 1, 0)
            v4 = get_vertex_index(i, j + 1, 0)
            faces.append([v1, v2, v3])
            faces.append([v1, v3, v4])
    
    # Create side faces between top surface vertices and bottom surface
    for i in range(rows - 1):
        for j in range(cols - 1):
            # Side faces between top vertices
            v1 = get_vertex_index(i, j, height_map[i, j])
            v2 = get_vertex_index(i + 1, j, height_map[i + 1, j])
            v3 = get_vertex_index(i, j + 1, height_map[i, j + 1])
            v4 = get_vertex_index(i + 1, j + 1, height_map[i + 1, j + 1])
            v5 = get_vertex_index(i, j, 0)
            v6 = get_vertex_index(i + 1, j, 0)
            v7 = get_vertex_index(i, j + 1, 0)
            v8 = get_vertex_index(i + 1, j + 1, 0)

            # Front faces
            faces.append([v1, v2, v6])
            faces.append([v1, v6, v5])
            # Right faces
            faces.append([v2, v4, v8])
            faces.append([v2, v8, v6])
            # Back faces
            faces.append([v3, v4, v8])
            faces.append([v3, v8, v7])
            # Left faces
            faces.append([v1, v3, v7])
            faces.append([v1, v7, v5])
    
    vertices = np.array(vertices)
    faces = np.array(faces)
    
    surface = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            surface.vectors[i][j] = vertices[f[j], :]
    
    surface.save(output_path)

if __name__ == "__main__":
    input_image_path = "C:/Users/Florian/Downloads/asd.jpg"  # Replace with your image file path
    output_stl_path = "output5.stl"  # Replace with your desired output STL file path
    
    resolution_scale = 0.25  # Adjust this value to scale the resolution (1.0 = original, 0.5 = half, etc.)
    max_height = 50.0  # Max height of the 3D model
    scale = 1.0  # Scale for the x and y dimensions of the model
    
    height_map = image_to_height_map(input_image_path, max_height=max_height, resolution_scale=resolution_scale)
    height_map_to_stl(height_map, output_stl_path, scale=scale)
