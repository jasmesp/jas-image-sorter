import os

pic_dir = "/Users/jasbook/Pictures/22_09_13-copy"


# def get_extensions(folder):
#     os.chdir(folder)
#     files = os.listdir(folder)
#     all_extensions = []
#     for file in files:
#         all_extensions.append(file.split(".")[-1])
#     return list(set(all_extensions))


def get_extensionsv2(folder):
    os.chdir(folder)
    files = os.listdir(folder)
    all_extensions = []
    for file in files:
        all_extensions.append(os.path.splitext(file))
    return list(set(all_extensions))


pretty = get_extensionsv2(pic_dir)
n = 0
x = len(pretty)
print(x)


def fraking_vars(list):
    for i in range(x):
        eff = list[i]
        effstr = str(f"{eff}")
        print(effstr.split(", "))
        print(eff, "\n")


def assign_var(list):
    ivar = 0
    print(list)
    for thing in list:
        ivar += 1
        zed = f"var{ivar} = {thing}"
        return zed


new_list = []
for i in pretty:
    new_list.append(i[1])

print(new_list)
# fraking_vars(pretty)
# print(assign_var(pretty))
