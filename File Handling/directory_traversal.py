import os


def traverse_dir(current_path, extensions):
    for elem in os.listdir(current_path):
        if os.path.isdir(os.path.join(current_path, elem)):
            traverse_dir(os.path.join(current_path, elem), extensions)
        else:
            extension = elem.split(".")[-1]
            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(elem)


extensions = {}
traverse_dir(".", extensions)

for ext, files in sorted(extensions.items()):
    print(f" .{ext}")
    for file in sorted(files):
        print(f"--- {file}")

