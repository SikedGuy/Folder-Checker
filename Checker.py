import os

def SearchDirectory(path: str)-> list[str]:
    folders: list[str] = []

    for item in os.listdir(path):
        i = 0

        # Check if item is a directory
        if (not os.path.isdir(os.path.join(path, item))):
            continue

        for item2 in os.scandir(os.path.join(path, item)):
            i += 1

        if (i <= 1):
            folders.append(item)

    return folders

username = input("<enter your username>")
directory = f"C:\\Users\\{username}\\AppData\\LocalLow\\Stress Level Zero\\BONELAB\\Mods"

folders = SearchDirectory(directory)

if (folders.__len__() <= 0):
    print("\nEverything looks good :)\n")
else:
    print(f"{folders.__len__()} possible bad folders found in [{directory}]")
    print("|")
    for folder in folders:
        print(f"|-> {folder}")

input("\nenter anything to close")
