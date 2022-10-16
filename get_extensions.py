import os

pic_dir = "/Users/jasbook/Pictures/22_09_13-copy"


def get_extensions(folder):
    os.chdir(folder)
    files = os.listdir(folder)
    all_extensions = []
    for file in files:
        all_extensions.append(file.split(".")[-1])
    return list(set(all_extensions))

def get_extensionsv2(folder):
    os.chdir(folder)
    files = os.listdir(folder)
    all_extensions = []
    for file in files:
        all_extensions.append(os.path.splitext(file))
    return list(set(all_extensions))

sex = get_extensionsv2(pic_dir)
n = 0
for x in sex:
    print(f"{x}\n")
i = 0

for i in range(len(sex)):
    print(sex[(i)])



sexy = str(sex)
remove = "[(',)]"
splitsexy = sexy.strip(remove)

print(splitsexy)
print(sex)
print("\n", sexy)
