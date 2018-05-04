import unittest
import os
import shutil
import io
import unittest.mock


import  supertool.files_handler

class TestDirectoryInspector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.mkdir('dir')
        with open(os.path.join('dir','workfile.txt'),'w') as file:
            file.write("I'm the file for test")
        with open(os.path.join('dir','file.txt'),'w') as file:
            file.write("I'm the file for test")
        with open(os.path.join('dir','example.txt'),'w') as file:
            file.write("I'm the file for test")
        os.mkdir(os.path.join('dir','subdir'))
        with open(os.path.join('dir','subdir','new.txt'),'w') as file:
            file.write('ararararaara')
        with open(os.path.join('dir','subdir','old.txt'),'w') as file:
            file.write('ararararaara')
        with open(os.path.join('dir','subdir','funnyjoke.txt'),'w') as file:
            file.write('Teacher: Do you have trouble making decisions? '
                       'Student: Well...yes and no.')
        with open(os.path.join('dir','subdir','unfunnyjoke.txt'),'w') as file:
            file.write('Teacher: Do you have trouble making decisions? '
                       'Student: Well...yes and no.')
        os.mkdir(os.path.join('dir','subdir2'))
        with open(os.path.join('dir','subdir2','anothernotfulljoke.html'),'w') as file:
            file.write('Teacher: Do you have trouble making decisions? ')
        with open(os.path.join('dir','subdir2','example.txt'),'w') as file:
            file.write("I'm the file for test")
        with open(os.path.join('dir','subdir2','notfulljoke.html'),'w') as file:
            file.write('Teacher: Do you have trouble making decisions? ')
        os.mkdir(os.path.join('dir','subdir3'))
        with open(os.path.join('dir','subdir3','alonefile.txt'), 'w') as file:
            file.write("I'm full of I'm full of loneliness")
        os.mkdir(os.path.join('dir','emptydirectory'))


    def setUp(self):
        self.di = supertool.files_handler.DirectoryInspection(os.path.join('.','dir'))

    def test_attribute(self):
        self.assertEqual(self.di.directory, os.path.join('.','dir'))

    def test_instance_with_incorrect_directory_negative(self):
        with self.assertRaises(FileNotFoundError) as raised_exception:
            supertool.files_handler.DirectoryInspection('Is not direcotory')
        self.assertEqual(raised_exception.exception.args[0], 'no such direcotory Is not direcotory',
                     'Values of exception wrong')

    def test_instance_with_incorrect_directory_not_str_negative(self):
        with self.assertRaises(TypeError) as raised_exception:
            supertool.files_handler.DirectoryInspection((1, 2))
        self.assertEqual(raised_exception.exception.args[0], 'directory must be str',
                     'Values of exception wrong')

    def test_get_file_hash_with_correct_values(self):
        self.assertEqual(self.di.get_file_hash('dir','example.txt'),('e2591d4b912cb8dd0a2030988b3feacf', 'example.txt'))

    def test_get_file_hash_with_incorrect_root(self):
        with self.assertRaises(TypeError) as raised_exception:
            self.di.get_file_hash(123,'sometext')
        self.assertEqual(raised_exception.exception.args[0], 'root must be str',
                         'Values of exception wrong')

    def test_get_file_hash_with_incorrect_root_file(self):
        with self.assertRaises(TypeError) as raised_exception:
            self.di.get_file_hash('.',31)
        self.assertEqual(raised_exception.exception.args[0], 'file must be str',
                         'Values of exception wrong')

    def test_get_file_hash_with_incorrect_path_to_root(self):
        with self.assertRaises(FileNotFoundError) as raised_exception:
            self.di.get_file_hash('Is not direcotory','as')
        self.assertEqual(raised_exception.exception.args[0], 'No such directory Is not direcotory',
                     'Values of exception wrong')

    def test_get_file_hash_with_incorrect_path_to_file(self):
        with self.assertRaises(FileNotFoundError) as raised_exception:
            self.di.get_file_hash('.','Is not direcotory')
        self.assertEqual(raised_exception.exception.args[0], 'No such file: Is not direcotory',
                     'Values of exception wrong')

    def test_get_similar_files_with_incorrect_value(self):
        with self.assertRaises(TypeError) as raised_exception:
            self.di.get_similar_files('.')
        self.assertEqual(raised_exception.exception.args[0], 'files_with_hash must be dict',
                         'Values of exception wrong')

    def test_get_similar_with_correct_input(self):
        self.assertEqual(self.di.get_similar_files({"hash":['andrey', 'tests', 'somefile']}),
                         [['andrey', 'tests', 'somefile']])
        self.assertEqual(self.di.get_similar_files({"hash": []}),
                         [])

    def test_identical_files_inspect(self):
        self.assertEqual(self.di.identical_files_inspect(),
                        [['example.txt', 'file.txt', 'workfile.txt', 'example.txt'],
                              ['funnyjoke.txt', 'unfunnyjoke.txt'], ['new.txt', 'old.txt'],
                              ['anothernotfulljoke.html', 'notfulljoke.html']])
        self.assertEqual(supertool.files_handler.DirectoryInspection(os.path.join('.', 'dir', 'emptydirectory')).identical_files_inspect(),
                                                                     [])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_get_copies_with_incorrrect_pass(self, mock_stdout):
        self.assertEqual(supertool.files_handler.get_copies('geron'), None)
        self.assertEqual(mock_stdout.getvalue(), 'FileNotFoundError: No such directory geron\n',
                         'Print did not work')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_get_copies_with_no_inspected_list(self, mock_stdout):
        self.assertEqual(supertool.files_handler.get_copies(os.path.join('dir','emptydirectory')), None)
        self.assertEqual(mock_stdout.getvalue(), 'In directory dir\emptydirectory\n'
                                                 'There are no identical files\n',
                         'Print did not work')

    def test_get_copies_with_no_similar_files(self):
        self.assertEqual(supertool.files_handler.get_copies(os.path.join('dir', 'subdir3')), None)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_get_copies_with_correct_input(self,  mock_stdout):
        self.assertEqual(supertool.files_handler.get_copies(os.path.join('dir')), None)
        self.assertEqual(mock_stdout.getvalue(), 'In directory dir\n'
                                                 '4 identical files: example.txt; file.txt; workfile.txt; example.txt\n'
                                                 '2 identical files: funnyjoke.txt; unfunnyjoke.txt\n'
                                                 '2 identical files: new.txt; old.txt\n'
                                                 '2 identical files: anothernotfulljoke.html; notfulljoke.html\n',
                         'Print did not work')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree('dir')


if __name__ == '__main__':
    unittest.main()
