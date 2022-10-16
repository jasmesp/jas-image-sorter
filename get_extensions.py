import os

pic_dir = "/Users/jasbook/Pictures/22_09_13-copy"


def get_extensions(folder):
    os.chdir(folder)
    files = os.listdir(folder)
    all_extensions = []
    for file in files:
        all_extensions.append(file.split(".")[-1])
    return list(set(all_extensions))


print(get_extensions(pic_dir))
