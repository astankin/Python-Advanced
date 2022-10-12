from os import walk

extensions = {}
for _, _, files in walk("."):
    for file in files:
        extension = file.split(".")[-1]
        if extension not in extensions:
            extensions[extension] = []
        extensions[extension].append(file)

for ext, files in sorted(extensions.items()):
    print(f" .{ext}")
    for file in sorted(files):
        print(f"--- {file}")
