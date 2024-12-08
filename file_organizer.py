import os
import shutil

# Define file type categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".odt"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".py", ".java", ".cpp", ".js", ".html", ".css"],
    "Others": []
}

def organize_files(directory):
    """
    Organizes files in the given directory into subfolders based on their extensions.
    
    Args:
        directory (str): The path to the directory to organize.
    """
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    # Create subfolders for each category
    for category in FILE_CATEGORIES.keys():
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # Move files to the appropriate category folder
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):  # Only process files
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(directory, category, filename))
                    moved = True
                    break

            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", filename))
    
    print(f"Files in '{directory}' have been organized.")

if __name__ == "__main__":
    directory_to_organize = input("Enter the path of the directory to organize: ").strip()
    organize_files(directory_to_organize)
