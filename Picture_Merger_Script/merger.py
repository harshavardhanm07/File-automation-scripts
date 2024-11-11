import os
import shutil

def merge_images(src_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Walk through the source directory and its subdirectories
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # Check if the file has an image extension
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.tif')):
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)

                # Make sure filename is unique in the destination directory
                unique_suffix = 1
                while os.path.exists(dest_file_path):
                    name, extension = os.path.splitext(file)
                    new_file_name = f"{name}_{unique_suffix}{extension}"
                    dest_file_path = os.path.join(dest_dir, new_file_name)
                    unique_suffix += 1

                # Copy the file to the destination directory
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied {src_file_path} to {dest_file_path}")

if __name__ == "__main__":
    # Set these paths according to your setup
    src_directory = r''  # Source directory
    dest_directory = r''  # Destination directory

    merge_images(src_directory, dest_directory)
    print("All images have been merged into the destination folder.")