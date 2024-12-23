import os
import json

# Directory containing images
IMAGES_DIR = './images'
OUTPUT_FILE = 'image-list.json'

# Helper function to recursively gather images
def gather_images(directory):
    images = []
    subdirectories = {}

    for entry in os.scandir(directory):
        if entry.is_file() and entry.name.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
            images.append(entry.name)
        elif entry.is_dir():
            subdirectories[entry.name] = gather_images(entry.path)

    return {"images": images, "subdirectories": subdirectories}

# Main function
def generate_image_list():
    data = gather_images(IMAGES_DIR)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    generate_image_list()
    print(f"Image list generated in {OUTPUT_FILE}")
