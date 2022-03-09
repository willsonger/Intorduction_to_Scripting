def check_files_if_exists():
    try:
        with open(f1.txt) as f:
            print("file present")
        except FileNotFoundError:
            print('file is not present')
        
