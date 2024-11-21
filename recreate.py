import os

def recreate_directory_structure(map_file, output_root):
    """
    Recreates a directory structure and files based on the provided map file.

    Args:
        map_file (str): The file containing the directory map and file contents.
        output_root (str): The root directory where the structure will be recreated.
    """
    current_dir = None
    current_file = None
    buffer = []

    def write_buffer_to_file(file_path, buffer):
        """Writes buffered lines to the specified file."""
        if not buffer:
            return
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(buffer)

    with open(map_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()  # Remove trailing newline and whitespace

            # Handle new directory
            if line.startswith("Directory:"):
                if current_file and buffer:
                    write_buffer_to_file(current_file, buffer)
                buffer = []  # Reset buffer
                current_file = None
                relative_dir = line.split("Directory:")[1].strip()
                current_dir = os.path.join(output_root, relative_dir)
                os.makedirs(current_dir, exist_ok=True)

            # Handle new file
            elif line.startswith("  File:"):
                if current_file and buffer:
                    write_buffer_to_file(current_file, buffer)
                buffer = []  # Reset buffer
                filename = line.split("File:")[1].strip()
                current_file = os.path.join(current_dir, filename)

            # Handle file content
            elif line.startswith("    "):  # Indentation indicates content
                buffer.append(line[4:] + "\n")  # Remove leading spaces and add a newline

        # Write any remaining buffer for the last file
        if current_file and buffer:
            write_buffer_to_file(current_file, buffer)

if __name__ == "__main__":
    # Input the map file and output root directory
    input_map_file = input("Enter the map file (e.g., directory_map.txt): ").strip()
    output_directory = input("Enter the root directory to recreate the structure: ").strip()
    
    recreate_directory_structure(input_map_file, output_directory)
    print(f"Directory structure recreated in: {output_directory}")
