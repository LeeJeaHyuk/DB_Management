# Completing the unfinished code to check some of the created images

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

# Clear contents of root path, create new folder hierarchy and images
clear_contents_of_root_path(root_path)
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
created_images_sample
