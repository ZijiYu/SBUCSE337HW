class FS_Item:
    def __init__(self, name):
        self.name = name

class Folder(FS_Item):
    def __init__(self, name):
        super().__init__(name)
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class File(FS_Item):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

def load_fs(ls_output):
    with open(ls_output, 'r') as f:
        lines = f.readlines()

    root = None
    current_path = []
    folders = {}

    for line in lines:
        line = line.strip()
        if line.endswith(':'):  # New directory
            dir_path = line[:-1]  # Remove ‘:’
            folder_name = dir_path.split('/')[-1]  # Get the last part as folder name
            folder = Folder(folder_name)
            folders[dir_path] = folder

            if not root:  # First directory is the root
                root = folder
            else:  # Add to parent folder
                parent_path = ' '.join(dir_path.split('/')[:-1])
                if parent_path in folders:
                    folders[parent_path].add_item(folder)

            current_path = dir_path
        elif 'total' in line or not line:
            continue  # Skip total line and empty lines
        else:  # Files
            parts = line.split()
            file_name = parts[-1]
            file_size = int(parts[-5])
            file = File(file_name, file_size)
            folders[current_path].add_item(file)

    return root

