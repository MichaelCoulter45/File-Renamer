from pathlib import Path




PATH_INPUT = Path("./input")
def file_renamer():
    """ Rename a folder of files to 'File {count}{suffix}' """
    for count, file_path in enumerate(PATH_INPUT.iterdir(), start=1):
        if file_path.is_file():
            # Renames using the original name stem and keeping the file type suffix
            new_name = f"New_File {count}{file_path.suffix}"
            new_file_path = file_path.with_name(new_name)
            try:
                file_path.rename(new_file_path)
                print(f"Renamed: \t{file_path.name}\t -->\t{new_name}")
            except FileNotFoundError:
                print("The source file does not exist.")
            except PermissionError:
                print("Permission denied. Check if the file is open elsewhere.")
            except FileExistsError:
                print(f"Cannot create a file when there's already a file with that name. {file_path}\t-->\t{new_name}")
####
def main():
    file_renamer()
if __name__ == "__main__":
    main()

