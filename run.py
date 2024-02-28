#           notMilitary Aviation Cognitive Testing
#                DO NOT REPRODUCE OR RELEASE

from home_screen import homeScreenWindow
from AirborneNumerical_screen import airborneNumericalWindow

from PySide2 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class window(qtw.QWidget): # This

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialise application classes to self
        self.home = homeScreenWindow()
        self.airborneNumerical = airborneNumericalWindow()



        # Create application window objects
        self.home = qtw.QMainWindow()
        self.airborneNumerical = qtw.QMainWindow()

        # Setup UI in window objects
        self.home.

        # Add function call to the buttons when clicked.
        self.ui = Home_screenUI()
        self.ui.setupUi(self)




if __name__ == '__main__':
    # Magic in order to make PyQT5 (the GUI framework) actually work.
    app = qtw.QApplication([])

    widget = window()
    widget.show()

    app.exec_()





