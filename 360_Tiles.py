import os
from PIL import Image

# Increase the maximum image pixel count to avoid DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = 999999999

# Loop through each image in the directory
for filename in os.listdir('.'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load the image and set the maximum pixel count
        img = Image.open(filename)
        img.thumbnail((999999999, 999999999), Image.LANCZOS)

        # Get the size of the image
        width, height = img.size

        # Ask the user for the number of tiles to create
        num_tiles = int(input(f"How many tiles do you want to create for {filename}? "))

        # Calculate the width and height of each tile image
        tile_width = int(width / 3)
        tile_height = int(height / (num_tiles / 3))

        # Create the directory for the tile images for the current image if it does not exist
        output_dir = os.path.join('Tiles', os.path.splitext(filename)[0] + '_tiles')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Loop through each tile
        for i in range(num_tiles // 3):
            for j in range(3):
                # Calculate the position of the current tile
                left = j * tile_width
                upper = i * tile_height
                right = left + tile_width
                lower = upper + tile_height

                # Select the portion of the image for the tile
                tile = img.crop((left, upper, right, lower))

                # Set the maximum pixel count for the tile using LANCZOS filter
                tile.thumbnail((999999999, 999999999), Image.LANCZOS)

                # Save the tile image with a sequential number in the same format as the input image
                tile_num = i * 3 + j + 1
                tile_ext = os.path.splitext(filename)[1]
                tile_name = f"{os.path.splitext(filename)[0]}_{tile_num:03}{tile_ext}"
                tile_path = os.path.join(output_dir, tile_name)
                tile.save(tile_path)

print("The tile images were created successfully.")
