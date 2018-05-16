"""
Window application for weather forecast.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from supertool.weather_gui._weather_gui import Ui_MainWindow
from supertool.weather_gui import _updated_weather as uw

class MainApp(QtWidgets.QMainWindow):
    """
    Main application of the package.
    """
    def __init__(self):
        """
        Initialize main application.
        """
        super(MainApp, self).__init__()
        self.place = ''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.get_button.clicked.connect(self.get_forecast)

    def get_forecast(self):
        """
        Method to handle pressure on get_button.

        :return: None.
        """
        try:
            self.place = self.ui.lineEdit.text()
            # delete all objects in grid.
            self._clear_grid(self.ui.gridLayout)
            self._clear_grid(self.ui.gridLayout_3)
            if not self.place:

                label = QtWidgets.QLabel(
                    'Please enter a place',
                    self.ui.gridLayoutWidget
                )
                label.setObjectName("labelerror")
                self.ui.gridLayout.addWidget(label, 0, 0, 1, 1)
            else:
                #request to update_weather module to get data.
                self.data = uw.get_weather(uw.get_weather_by_coordinates(
                    uw.get_coordinates(self.place),
                    'weather')
                )
                #dinamically create buttons with current weather and forecast.
                cweather_button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
                sizePolicy = QtWidgets.QSizePolicy(
                    QtWidgets.QSizePolicy.Ignored,
                    QtWidgets.QSizePolicy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(cweather_button.sizePolicy().hasHeightForWidth())
                cweather_button.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Segoe UI Black")
                font.setBold(True)
                font.setWeight(75)
                cweather_button.setFont(font)
                cweather_button.setObjectName("cweather_button")
                self.ui.gridLayout.addWidget(cweather_button, 0, 0, 1, 1)
                #create second button
                fweather_button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
                font = QtGui.QFont()
                font.setFamily("Segoe UI Black")
                font.setBold(True)
                font.setWeight(75)
                fweather_button.setFont(font)
                fweather_button.setObjectName("fweather_button")
                self.ui.gridLayout.addWidget(fweather_button, 0, 1, 1, 1)
                #bind buttons with methods
                cweather_button.clicked.connect(self.current_weather)
                fweather_button.clicked.connect(self.forecast_weather)
                #set names
                cweather_button.setText("Current weather")
                fweather_button.setText("Weather forecast")
                #show them
                cweather_button.show()
                fweather_button.show()
                self.current_weather()

        except Exception as exc:
            #in case exception delete all objects in grid layout 3 and 1.
            self._clear_grid(self.ui.gridLayout)
            self._clear_grid(self.ui.gridLayout_3)
            #put error message in grid layout 1
            error_massage = f'Error: {exc.args[0]}'
            label = QtWidgets.QLabel(error_massage, self.ui.gridLayoutWidget)
            label.setObjectName("labelerror")
            self.ui.gridLayout.addWidget(label, 0, 0, 1, 1)

    def current_weather(self):
        """
        Method to handle pressure on cwather_button.

        :return: None.
        """
        #clear grid
        self._clear_grid(self.ui.gridLayout_3)
        #dinamically create table
        tableWidget = QtWidgets.QTableWidget(len(self.data.keys()), 1, self.ui.gridLayoutWidget_3)
        tableWidget.setObjectName("tableWidget_0")
        self.ui.gridLayout_3.addWidget(tableWidget, 0, 0, 1, 1)
        #font for elements in table
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(175)
        #smthg like name of table
        tableWidget.setHorizontalHeaderLabels([f'Current weather in {self.place}'])
        tableWidget.horizontalHeaderItem(0).setFont(font)
        tableWidget.setVerticalHeaderLabels(list(self.data.keys()))
        header = tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        vertical = tableWidget.verticalHeader()
        vertical.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #fill all elements in table
        for i, v in enumerate(self.data.values()):
            font.setPointSize(16)
            tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(v).center(60)))
            tableWidget.item(i, 0).setFlags(QtCore.Qt.ItemIsEnabled)
            tableWidget.item(i, 0).setFont(font)

    def forecast_weather(self):
        """
        Method to handle pressure on fwather_button.

        :return: None.
        """
        #create variable for position of dates and values
        date_pos = 0
        value_pos = 1
        #request to updated weather to get forecast.
        data = uw.get_pretty_nice_table(self.place)
        forecast_dates = data[0]
        forecast_data = data[1]
        #clear grid
        self._clear_grid(self.ui.gridLayout_3)
        #dinamycally create and fill all data
        for index, val in enumerate(forecast_data):
            label = QtWidgets.QLabel(forecast_dates[index], self.ui.gridLayoutWidget_3)
            label.setObjectName(f"label{date_pos}")
            self.ui.gridLayout_3.addWidget(label, date_pos, 0, 1, 1)
            tableWidget = QtWidgets.QTableWidget(len(self.data.keys()),
                                                 3, self.ui.gridLayoutWidget_3)
            tableWidget.setObjectName(f"tableWidget{index}")
            self.ui.gridLayout_3.addWidget(tableWidget, value_pos, 0, 1, 1)
            tableWidget.setHorizontalHeaderLabels(uw.get_day_time())
            tableWidget.setVerticalHeaderLabels(list(self.data.keys()))
            tableWidget.setTextElideMode(3)
            header = tableWidget.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            for count, value in enumerate(val):
                for num, elem in enumerate(value):
                    tableWidget.setItem(
                        count,
                        num,
                        QtWidgets.QTableWidgetItem(str(elem).center(10))
                    )
                    font = QtGui.QFont()
                    font.setFamily("Segoe UI Black")
                    font.setBold(True)
                    font.setWeight(75)
                    tableWidget.item(count, num).setFlags(QtCore.Qt.ItemIsEnabled)
                    tableWidget.item(count, num).setFont(font)
            date_pos += 2
            value_pos += 2

    def _clear_grid(self, grid):
        """
        Method to clear grid.
        :param grid: GridLayout.
        :return: None.
        """
        for i in reversed(range(grid.count())):
            grid.itemAt(i).widget().deleteLater()



if __name__ == '__main__':
    pass
