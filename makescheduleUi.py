from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class WriteScheduleUi(object):
    def __init__(self):
        self.mainwindow=QtWidgets.QMainWindow()
        self.mainwindow.resize(350,700)
        self.SetupUi()
        self.mainwindow.show()
        
    def SetupUi(self):
        self.paper=QtWidgets.QWidget(self.mainwindow)
        self.paper.resize(350,700)
        self.paper.setStyleSheet('background:white;')

        self.mondaylabel=QtWidgets.QLabel(self.paper)
        self.mondaylabel.setGeometry(10,30,100,22)
        self.mondaylabel.setStyleSheet("background:white;")
        self.mondaylabel.setText("월요일")
        self.mondaylineedit=QtWidgets.QLineEdit(self.paper)
        self.mondaylineedit.setGeometry(80,30,130,22)

        self.thusdaylabel=QtWidgets.QLabel(self.paper)
        self.thusdaylabel.setGeometry(10,80,100,22)
        self.thusdaylabel.setStyleSheet("background:white;")
        self.thusdaylabel.setText("화요일")
        self.thusdaylineedit=QtWidgets.QLineEdit(self.paper)
        self.thusdaylineedit.setGeometry(80,80,130,22)

        self.wendsdaylabel=QtWidgets.QLabel(self.paper)
        self.wendsdaylabel.setGeometry(10,130,100,22)
        self.wendsdaylabel.setStyleSheet("background:white;")
        self.wendsdaylabel.setText("수요일")
        self.wendsdaylineedit=QtWidgets.QLineEdit(self.paper)
        self.wendsdaylineedit.setGeometry(80,130,130,22)

        self.thirsdaylabel=QtWidgets.QLabel(self.paper)
        self.thirsdaylabel.setGeometry(10,180,100,22)
        self.thirsdaylabel.setStyleSheet("background:white;")
        self.thirsdaylabel.setText("목요일")
        self.thirsdaylineedit=QtWidgets.QLineEdit(self.paper)
        self.thirsdaylineedit.setGeometry(80,180,130,22)

        self.fridaylabel=QtWidgets.QLabel(self.paper)
        self.fridaylabel.setGeometry(10,230,100,22)
        self.fridaylabel.setStyleSheet("background:white;")
        self.fridaylabel.setText("금요일")
        self.fridaylineedit=QtWidgets.QLineEdit(self.paper)
        self.fridaylineedit.setGeometry(80,230,130,22)

        self.mondaybutton=QtWidgets.QPushButton(self.paper)
        self.mondaybutton.setGeometry(260,30,70,22)
        self.mondaybutton.setText("월요일")

        self.thusdaybutton=QtWidgets.QPushButton(self.paper)
        self.thusdaybutton.setGeometry(260,80,70,22)
        self.thusdaybutton.setText("화요일")

        self.wendsdaybutton=QtWidgets.QPushButton(self.paper)
        self.wendsdaybutton.setGeometry(260,130,70,22)
        self.wendsdaybutton.setText("수요일")

        self.thirsdaybutton=QtWidgets.QPushButton(self.paper)
        self.thirsdaybutton.setGeometry(260,180,70,22)
        self.thirsdaybutton.setText("목요일")

        self.fridaybutton=QtWidgets.QPushButton(self.paper)
        self.fridaybutton.setGeometry(260,230,70,22)
        self.fridaybutton.setText("금요일")

        self.applybutton=QtWidgets.QPushButton(self.paper)
        self.applybutton.setGeometry(200,500,100,22)
        self.applybutton.setText('적용하기')

        





if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    asdf=WriteScheduleUi()
    sys.exit(app.exec_())