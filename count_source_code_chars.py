

import os





def count(dir_path:str, include_extensions=None)->int:

    def count_lines_of_file(path:str)->int:
        with open(path, "r") as f1:
            return f1.read().count("\n")

    if include_extensions is None:
        include_extensions = [".py"]
    walker = os.walk(dir_path)
    counter:int = 0
    for dirpath, dirnames, filenames in walker:
        for i1 in filenames:
            ext = os.path.splitext(i1)[1]

            if ext in include_extensions and ".idea" not in dirpath and ".git" not in dirpath:
                counter += count_lines_of_file(dirpath+"//"+i1)

    return counter

if __name__ == "__main__":
    print(count("../cooper"))