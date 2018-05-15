"""
Updated module to inspect directory on similar files
for gui representations.
"""
import hashlib
import os


BUFSIZE = 65536

class DirectoryInspection:
    """
    Class to inspect directory on similar files.
    """
    def __init__(self, directory='.'):
        """
        Initialize an instance.

        :param directory: directory that needs inspect.
        :type directory: str.
        :raises: TypeError, SystemExit.

        Usage
        >>> di = DirectoryInspection('.')
        >>> di.directory
        '.'
        """
        if not isinstance(directory, str):
            raise TypeError('directory must be str')
        if not os.path.isdir(directory):
            raise FileNotFoundError(f'no such direcotory {directory}')
        self.directory = directory

    def get_file_hash(self, root, file):
        """
        Method to get hash from some file.

        :param root: path to file.
        :type root: str.
        :param file: name of source file.
        :type file: str.
        :return: tuple -- hash and name of file.
        :raises: FileNotFoundError, TypeError.

        Usage
        >>> DirectoryInspection().get_file_hash('.','__init__.py')
        ('d41d8cd98f00b204e9800998ecf8427e', '__init__.py')
        """
        if not isinstance(root, str):
            raise TypeError("root must be str")
        if not isinstance(file, str):
            raise TypeError("file must be str")
        if not os.path.isdir(root):
            raise FileNotFoundError(f'No such directory {root}')
        if not os.path.isfile(os.path.join(root, file)):
            raise FileNotFoundError(f"No such file: {file}")
        with open(os.path.join(root, file), 'rb') as afile:
            hasher = hashlib.md5()
            buf = afile.read(BUFSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BUFSIZE)
            return hasher.hexdigest(), file


    def get_similar_files(self, files_with_hash):
        """
        Method to get all similar files from directory.

        :param root: path to files.
        :type root: str.
        :param files_with_hash: files with them hashes.
        :type files_with_hash: dict
        :return: tuple -- directory and similar files in it or None.
        :raises: FileNotFoundError, TypeError
        Usage
        >>> DirectoryInspection().get_similar_files({})
        []
        """
        if not isinstance(files_with_hash, dict):
            raise TypeError("files_with_hash must be dict")
        copies_directory = []
        if files_with_hash:
            for fhash, filenames in files_with_hash.items():
                if len(filenames) > 1:
                    copies_directory.append(filenames)
        return copies_directory

    def identical_files_inspect(self):
        """
        Method to inspect directory on similar files.

        :return: dict -- directory as key and list of list of similar files as value.
        """
        files_with_hash = {}
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                hashed_file = self.get_file_hash(root, file)
                files_with_hash.setdefault(hashed_file[0], []).append(hashed_file[1])
        inspected = self.get_similar_files(files_with_hash)
        return inspected

def get_copies(path):
    """
    Function to get similar files in directory.

    :param path: target directory.
    :type path:str.
    :return: list - data about inspection.
    :raises: FileNotFoundError.
    """
    result = []
    if not os.path.isdir(path):
        raise FileNotFoundError(f'No such directory {path}')
    inspector = DirectoryInspection(path)
    inspected = inspector.identical_files_inspect()
    if inspected:
        for similar_files in inspected:
            if similar_files:
                result.append(f'{len(similar_files)} identical files: ' + "; ".join(similar_files))
    else:
        result.append("There are no identical files")
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()