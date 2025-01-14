import os

def display_directory_structure(start_path, indent=""):
    for item in os.listdir(start_path):
        item_path = os.path.join(start_path, item)
        if os.path.isdir(item_path):
            print(f"{indent}├── {item}\\")
            display_directory_structure(item_path, indent + "│   ")
        else:
            print(f"{indent}├── {item}")

# Get the current working directory
current_directory = os.getcwd()
print(f"{current_directory}\\")
display_directory_structure(current_directory)
