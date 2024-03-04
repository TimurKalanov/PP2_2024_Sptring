def inf_about_path():
    path = r"C:\Users\вставляешь короче путь"
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