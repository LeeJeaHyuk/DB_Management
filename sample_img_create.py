import os
import random
from PIL import Image
import numpy as np
import shutil

def create_folder_hierarchy(root_path):
    # Define folder name options
    first_folder_names = ["Audio", "Image", "Video", "Text"]
    people_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]  # Example names
    artwork_names = ["Sunrise", "MysticRiver", "AutumnLeaves", "BlueHorizon", "NightSky"]  # Example artwork names

    # Create the root folder
    if not os.path.exists(root_path):
        os.makedirs(root_path)

    # Generate a random number of main folders (up to 4, as there are 4 types)
    num_main_folders = random.randint(1, 4)
    selected_first_folders = random.sample(first_folder_names, num_main_folders)

    for folder_name in selected_first_folders:
        # Create a main folder
        main_folder_path = os.path.join(root_path, folder_name)
        os.makedirs(main_folder_path, exist_ok=True)

        # Generate a random number of subfolders (up to 5)
        num_sub_folders = random.randint(1, 5)
        selected_people_names = random.sample(people_names, num_sub_folders)

        for person_name in selected_people_names:
            # Create a subfolder with a person's name
            sub_folder_path = os.path.join(main_folder_path, person_name)
            os.makedirs(sub_folder_path, exist_ok=True)

            # Generate a random number of image folders (up to 5)
            num_image_folders = random.randint(1, 5)
            selected_artwork_names = random.sample(artwork_names, num_image_folders)

            for artwork_name in selected_artwork_names:
                # Create an image folder with an artwork name
                image_folder_path = os.path.join(sub_folder_path, artwork_name)
                os.makedirs(image_folder_path, exist_ok=True)

def create_example_images(root_path):
    # Walking through the directory structure
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Split the directory path
        path_parts = dirpath.split(os.sep)

        # Check if the current directory is a subfolder under one of the main categories (Audio, Image, Video, Text)
        # and also check if it's an artwork subfolder (3 levels deep in 'Data' directory)
        if len(path_parts) == 4 and path_parts[1] in ["Audio", "Image", "Video", "Text"]:
            person_name = path_parts[2]  # Person's name
            artwork_name = path_parts[3]  # Artwork name

            # Generate a random number of images (up to 5)
            num_images = random.randint(1, 5)

            for i in range(num_images):
                # Create an example image
                image_data = np.random.rand(100, 100, 3) * 255  # Random RGB image
                image = Image.fromarray(image_data.astype('uint8')).convert('RGB')

                # Define image file path with person and artwork name
                image_file_path = os.path.join(dirpath, f"{person_name}_{artwork_name}_{i}.png")

                # Save the image
                image.save(image_file_path)

# Function to clear the root path before creating new folders
def clear_contents_of_root_path(root_path):
    # Check if the root path exists
    if os.path.exists(root_path):
        # Iterate through all files and directories inside the root path
        for filename in os.listdir(root_path):
            file_path = os.path.join(root_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Remove files and links
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Remove directories

# Define the root path
root_path = 'Data'

clear_contents_of_root_path(root_path)

# Now, you can recreate the folder hierarchy and images
create_folder_hierarchy(root_path)
create_example_images(root_path)

# Check some of the created images
created_images = []
for dirpath, _, filenames in os.walk(root_path):
    for filename in filenames:
        if filename.endswith('.png'):
            created_images.append(os.path.join(dirpath, filename))

# Displaying a sample of the created images
created_images_sample = created_images[:5]  # Displaying only the first 5 images
