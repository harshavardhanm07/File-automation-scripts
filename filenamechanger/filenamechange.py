import os

def rename_specific_files_with_counter(directory, file_extension, new_base_name):
    """Rename files with a specific extension in the specified directory with a new base name.
    If a file with the new name already exists, append a counter to prevent overwriting.

    Args:
        directory (str): The directory containing the files to rename.
        file_extension (str): The extension of the files to rename (e.g., '.jpg').
        new_base_name (str): The new base name without the extension.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"The specified path: '{directory}' is not a directory.")

    for filename in os.listdir(directory):
        # Check if file has the specified file extension
        if filename.endswith(file_extension):
            # Extract file extension
            name, ext = os.path.splitext(filename)

            # Initialize counter
            counter = 1
            new_name = f"{new_base_name}{ext}"
            new_file_path = os.path.join(directory, new_name)

            # Increment counter if file exists
            while os.path.exists(new_file_path):
                new_name = f"{new_base_name}{str(counter).zfill(4)}{ext}"
                new_file_path = os.path.join(directory, new_name)
                counter += 1

            # Rename the file
            original_file_path = os.path.join(directory, filename)
            os.rename(original_file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_name}'")

if __name__ == "__main__":
    directory_path = r"C:\Normal Heart Dataset"  # Source folder path
    file_extension = ".jpg"                      # Specify the file format you're interested in
    new_base_name = "sample"

    rename_specific_files_with_counter(directory_path, file_extension, new_base_name)