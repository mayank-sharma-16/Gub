import pathlib

# can technically be done in one line but 
def file_count(file_path, starting=""):
    initial_count = 0
    for path in pathlib.Path(file_path).iterdir():
        if path.is_file() and path.name.startswith(starting):
            initial_count += 1

    return initial_count