import os
import shutil

def organize_images(base_folder, output_folder="data"):
    """
    Renames and organizes images from subfolders into a single folder.

    Args:
        base_folder (str): Path to the base folder containing subfolders with images.
        output_folder (str): Path to the output folder where renamed images will be stored.

    Returns:
        None
    """
    # Supported image extensions
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif", ".webp"}

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Traverse through each subfolder
    for folder_name in os.listdir(base_folder):
        subfolder_path = os.path.join(base_folder, folder_name)

        # Check if it's a folder
        if os.path.isdir(subfolder_path):
            # Initialize counter for renaming
            counter = 1

            # Iterate over files in the subfolder
            for file_name in os.listdir(subfolder_path):
                file_path = os.path.join(subfolder_path, file_name)

                # Check if file is an image
                if os.path.splitext(file_name)[1].lower() in image_extensions:
                    # New file name: folder_name + counter
                    new_file_name = f"{folder_name}_{counter}.jpg"  # Change extension if needed
                    new_file_path = os.path.join(output_folder, new_file_name)

                    # Copy the image to the output folder with the new name
                    shutil.copy(file_path, new_file_path)
                    print(f"Copied and renamed: {file_path} -> {new_file_path}")

                    # Increment counter
                    counter += 1

    print(f"Images organized and saved in '{output_folder}'.")

# Example usage
base_folder = "PopularDropSpots"  # Replace with your folder's path
organize_images(base_folder)
