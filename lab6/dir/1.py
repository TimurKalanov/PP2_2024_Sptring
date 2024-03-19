import os
def inf_about_path():
    path = r"C:\Users\Timur\Documets\PP2\lab6\dir"
    print("Directories:")
    print(
        [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    )
    print("Files:")
    print(
        [
            name
            for name in os.listdir(path)
            if not os.path.isdir(os.path.join(path, name))
        ]
    )
    print("Directories and files :")
    print([name for name in os.listdir(path)])