import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = list()
    for file_or_dir in os.listdir(path):
        full_path = os.path.join(path, file_or_dir)
        if os.path.isfile(full_path) and full_path.endswith(suffix):
            files.append(full_path)
        elif os.path.isdir(full_path):
            output = find_files(suffix, full_path)
            files.extend(output)
    return files


print(find_files('.c', 'testdir'))

print(find_files('.c', 'testdir\\subdir2'))

print(find_files('.py', '.'))