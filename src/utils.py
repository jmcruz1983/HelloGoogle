"""
Module that setups paths and environment variables
"""
import os

def get_files(dir, exts):
    list_fs = []
    if dir and exts:
        for root, directories, filenames in os.walk(dir):
            for filename in filenames:
                for ext in exts:
                    if filename.endswith(ext):
                        list_fs.append(os.path.join(root,
                                                    filename))
                        break
    return list_fs


def check_files(dir=None, exts=None):
    return True if len(get_files(dir, exts)) > 0 else False

def find_file(dir=None, filename=None):
    found_files = []
    f_name, f_ext = os.path.splitext(filename)
    for _f in get_files(dir, [f_ext]):
        if _f.endswith(filename):
            found_files.append(_f)
    return found_files
