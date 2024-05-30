import os

def print_directory_structure(root_dir, indent=''):
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        print(indent + '|-- ' + item)
        if os.path.isdir(path):
            print_directory_structure(path, indent + '    ')

if __name__ == "__main__":
    root_dir = '.'  # You can change this to any directory you want to print
    print_directory_structure(root_dir)
