import os
import shutil

def process_files(input_folder, processed_folder):
    """
    Process files by moving them from the Input folder to the Processed folder
    and renaming them with a "_processed" suffix.
    """
    # Ensure the Processed folder exists
    os.makedirs(processed_folder, exist_ok=True)

    # Get the list of files in the Input folder
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    if not files:
        print("No files found in the Input folder.")
        return

    for file_name in files:
        # Define the full path of the source file
        source_path = os.path.join(input_folder, file_name)

        # Move the file to the Processed folder
        destination_path = os.path.join(processed_folder, file_name)
        shutil.move(source_path, destination_path)

        # Add "_processed" suffix to the file name
        file_base, file_extension = os.path.splitext(file_name)
        new_file_name = f"{file_base}_processed{file_extension}"
        new_file_path = os.path.join(processed_folder, new_file_name)

        # Rename the file in the Processed folder
        os.rename(destination_path, new_file_path)

    print(f"Processed {len(files)} file(s). They have been moved and renamed.")

if __name__ == "__main__":
    # Define the folder paths
    input_folder = "Input"
    processed_folder = "Processed"

    # Process the files
    process_files(input_folder, processed_folder)
