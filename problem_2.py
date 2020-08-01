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
    if os.path.exists(path):
        for file_or_dir in os.listdir(path):
            full_path = os.path.join(path, file_or_dir)
            if os.path.isfile(full_path) and full_path.endswith(suffix):
                files.append(full_path)
            elif os.path.isdir(full_path):
                output = find_files(suffix, full_path)
                files.extend(output)
        return files
    else:
        return 'No such directory'


print(find_files('.c', 'testdir'))
# ['testdir\subdir1\a.c', 'testdir\subdir3\subsubdir1\b.c', 'testdir\subdir5\a.c', 'testdir\t1.c']

print(find_files('.c', 'testdir\\subdir2'))
# []

print(find_files('.py', '.'))
# ['.\problem_1.py', '.\problem_2.py', '.\problem_3.py', '.\problem_4.py', '.\problem_5.py', '.\problem_6.py']

print(find_files('', 'testdir'))
# finds all files in testdir directory

print(find_files('', 'testdir1'))
