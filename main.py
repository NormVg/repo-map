import os

def create_filtered_directory_map(root_dir, output_file, excluded_dirs=None, excluded_files=None):
    """
    Walks through a directory and creates a map of its structure.
    Skips excluded directories and files, and includes the full contents of other files.

    Args:
        root_dir (str): The root directory to map.
        output_file (str): The file to write the directory map to.
        excluded_dirs (list): Directories to exclude.
        excluded_files (list): Files to exclude.
    """
    if excluded_dirs is None:
        excluded_dirs = [".git", "node_modules", "__pycache__","venv"]
    if excluded_files is None:
        excluded_files = [".gitignore"]

    with open(output_file, "w", encoding="utf-8") as out_file:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Filter out excluded directories
            dirnames[:] = [d for d in dirnames if d not in excluded_dirs]

            # Write the current directory
            relative_dir = os.path.relpath(dirpath, root_dir)
            if relative_dir == ".":
                relative_dir = root_dir
            out_file.write(f"\nDirectory: {relative_dir}\n")
            out_file.write("-" * 40 + "\n")
            
            # Write each file in the directory, skipping excluded files
            for filename in filenames:
                if filename in excluded_files:
                    continue
                file_path = os.path.join(dirpath, filename)
                out_file.write(f"  File: {filename}\n")
                
                # Include the full file content
                if os.path.isfile(file_path):
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            out_file.write("    Contents:\n")
                            out_file.write(f"{content}\n")
                    except Exception as e:
                        out_file.write(f"    [Could not read file: {e}]\n")
            out_file.write("\n")

if __name__ == "__main__":
    # Set the directory and output file
    directory_to_map = input("Enter the directory to map: ").strip()
    output_filename = input("Enter the output file name (e.g., directory_map_filtered.txt): ").strip()
    if not output_filename: output_filename = "directory_map_filtered.txt"
    create_filtered_directory_map(directory_to_map, output_filename)
    print(f"Filtered directory map has been saved to {output_filename}.")
