import smtplib
import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QDesktopWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from playsound import playsound
from threading import Thread
from PyQt5.QtCore import QDateTime, Qt

class WarningBox(QWidget):
    """Defining the parameters of the warning bow"""
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        instance = QDateTime.currentDateTime()
        text_displayed = "   WARNING! Error detected\n"+ instance.toString(Qt.DefaultLocaleLongDate)
        #self.setWindowIcon(QIcon('resources/warning_icon.png'))
        display = QLabel()
        display.setText(text_displayed)
        display.setAlignment(Qt.AlignHCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(display)
        vbox.addStretch()
        self.setLayout(vbox)
        self.setFixedHeight(300)
        self.setFixedWidth(400)
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 200)
        #self.setGeometry(500, 300, 300, 300)


        self.center()
        self.setWindowTitle('WARNING')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def warning_function():
    """Executing the warning message on call"""
    app = QApplication(sys.argv)
    ex = WarningBox()
    sys.exit(app.exec_())

def sound_loop():
    while True:
        playsound('resources/enough.mp3')


def start_alarm(sound=True, warning_message=True, email=False):
    """name is self explanatory"""

    if warning_message == True:
        ###throw up a warning Window, is a thread so that other functions can happen simultaneously
        t = Thread(target=warning_function)
        t.start()

    if sound == True:                       #fix this, the main program runs the side program

        h = Thread(target=sound_loop)
        h.daemon = True
        h.start()

    if email == True:                   ####  Clearly haven't implemented this yet
        ###read in emil list and send out warning email
        print("simulation email")



