"""
Window application to inspects directories on similar files.
"""
from PyQt5 import QtWidgets
from supertool.files_handler_gui._files_handler_gui import Ui_MainWindow
import supertool.files_handler_gui._updated_files_handler as fh

class MainApp(QtWidgets.QMainWindow):
    """
    Main application of the package.
    """
    def __init__(self):
        """
        Initialize main window.
        """
        super(MainApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.directory = self.ui.lineEdit.text()
        self.ui.browse_button.clicked.connect(self.browse_pressed)
        self.ui.inspect_button.clicked.connect(self.inspect_pressed)
        self.ui.label_2.hide()
        self.ui.listWidget.hide()

    def browse_pressed(self):
        """
        Method to handle pressure on browse button.

        :return:None.
        """
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        self.ui.lineEdit.setText(directory)
        self.directory = self.ui.lineEdit.text()

    def inspect_pressed(self):
        """
        Method to handle pressure on inspect button.

        :return: None.
        """
        try:
            if self.ui.lineEdit.text():
                data = self.get_similar_files()
                self.ui.label_2.show()
                self.ui.listWidget.show()
                self.ui.label_2.setText(f'Target: {self.ui.lineEdit.text()}')
                self.ui.listWidget.clear()
                self.ui.listWidget.addItems(data)
            else:
                self.ui.label_2.show()
                self.ui.listWidget.hide()
                self.ui.label_2.setText(f'Please enter or select directory')
        except Exception as exc:
            self.ui.label_2.show()
            self.ui.listWidget.hide()
            self.ui.label_2.setText(f'Error: {exc.args[0]}')

    def get_similar_files(self):
        """
        Method to find similar files in target directory.

        :return: list -- data
        """
        result = fh.get_copies(self.ui.lineEdit.text())
        return result



if __name__ == '__main__':
    pass
