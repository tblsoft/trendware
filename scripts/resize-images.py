from PIL import Image
import os

def optimize_and_resize_image(input_path, output_path, max_width=500, quality=85):
    # Open the image
    with Image.open(input_path) as img:
        # Calculate the new height to maintain the aspect ratio
        width_percent = (max_width / float(img.size[0]))
        new_height = int((float(img.size[1]) * float(width_percent)))

        # Resize the image
        img_resized = img.resize((max_width, new_height), Image.ANTIALIAS)

        # Save the image with optimization and reduced quality
        img_resized.save(output_path, format="JPEG", optimize=True, quality=quality)

def process_images_in_folder(input_folder, output_folder, max_width=500, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename).replace(".png", ".jpg")
            optimize_and_resize_image(input_path, output_path, max_width, quality)
            print(f"Processed {filename}")

# Usage example
input_folder = f"{base_path}/shop/data/img"
output_folder = f"{base_path}/shop/data/web-img"

process_images_in_folder(input_folder, output_folder, max_width=300, quality=60)