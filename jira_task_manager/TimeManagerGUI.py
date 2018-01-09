# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimeManagerGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

s = 0
m = 0
h = 0

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(520, 320)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_start = QtGui.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(180, 230, 100, 60))
        self.button_start.setObjectName(_fromUtf8("button_start"))
        self.button_reset = QtGui.QPushButton(self.centralwidget)
        self.button_reset.setGeometry(QtCore.QRect(290, 230, 100, 60))
        self.button_reset.setObjectName(_fromUtf8("button_reset"))
        self.button_log = QtGui.QPushButton(self.centralwidget)
        self.button_log.setGeometry(QtCore.QRect(400, 230, 100, 60))
        self.button_log.setObjectName(_fromUtf8("button_log"))
        self.label_task_type = QtGui.QLabel(self.centralwidget)
        self.label_task_type.setGeometry(QtCore.QRect(10, 80, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_task_type.setFont(font)
        self.label_task_type.setObjectName(_fromUtf8("label_task_type"))
        self.box_task_type = QtGui.QComboBox(self.centralwidget)
        self.box_task_type.setGeometry(QtCore.QRect(10, 110, 500, 30))
        self.box_task_type.setObjectName(_fromUtf8("box_task_type"))
        self.label_task_act = QtGui.QLabel(self.centralwidget)
        self.label_task_act.setGeometry(QtCore.QRect(10, 150, 110, 30))
        self.label_task_act.setFont(font)
        self.label_task_act.setObjectName(_fromUtf8("label_task_act"))
        self.taskActBox = QtGui.QComboBox(self.centralwidget)
        self.taskActBox.setGeometry(QtCore.QRect(10, 180, 500, 30))
        self.taskActBox.setObjectName(_fromUtf8("taskActBox"))
        self.label_user = QtGui.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(147, 15, 50, 20))
        self.label_user.setFont(font)
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.label_password = QtGui.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(100, 55, 100, 20))
        self.label_password.setFont(font)
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.edit_user = QtGui.QLineEdit(self.centralwidget)
        self.edit_user.setGeometry(QtCore.QRect(200, 10, 180, 30))
        self.edit_user.setObjectName(_fromUtf8("edit_user"))
        self.edit_password = QtGui.QLineEdit(self.centralwidget)
        self.edit_password.setGeometry(QtCore.QRect(200, 50, 180, 30))
        self.edit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.edit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_password.setObjectName(_fromUtf8("edit_password"))
        self.button_login = QtGui.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(400, 15, 100, 60))
        self.button_login.setObjectName(_fromUtf8("button_login"))
        self.lcd = QtGui.QLCDNumber(self.centralwidget)
        self.lcd.setGeometry(QtCore.QRect(10, 230, 160, 60))
        self.lcd.setObjectName(_fromUtf8("lcdNumber"))
        init_time = str('00:00:00')
        self.lcd.setDigitCount(len(init_time))
        self.lcd.display(init_time)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSet_login = QtGui.QAction(MainWindow)
        self.actionSet_login.setObjectName(_fromUtf8("actionSet_login"))

        self.dialog = MyDialog(self)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)

        self.button_start.clicked.connect(self.start)
        self.button_reset.clicked.connect(self.reset)
        self.button_log.clicked.connect(self.log_task)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.clock_started= False

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Task Logger", None))
        self.button_start.setText(_translate("MainWindow", "START", None))
        self.button_reset.setText(_translate("MainWindow", "RESET", None))
        self.button_log.setText(_translate("MainWindow", "LOG TASK", None))
        self.label_task_type.setText(_translate("MainWindow", "Task Type", None))
        self.label_task_act.setText(_translate("MainWindow", "Task Activity", None))
        self.label_user.setText(_translate("MainWindow", "USER:", None))
        self.label_password.setText(_translate("MainWindow", "PASSWORD:", None))
        self.button_login.setText(_translate("MainWindow", "Login", None))
        self.actionSet_login.setText(_translate("MainWindow", "Set login", None))
        self.button_start.setDisabled(True)
        self.button_reset.setDisabled(True)
        self.button_log.setDisabled(True)
        self.taskActBox.setDisabled(True)
        self.box_task_type.setDisabled(True)

    def enable_buttons(self):
        self.button_start.setDisabled(False)
        self.button_reset.setDisabled(False)
        self.button_log.setDisabled(False)
        self.taskActBox.setDisabled(False)
        self.box_task_type.setDisabled(False)

    def set_user(self, user):
        self.edit_user.setText(str(user))

    def add_task_types(self, task_types_list):
        for item in task_types_list:
            self.box_task_type.addItem(item)

    def add_task_activities(self, list_of_tickets):
        self.taskActBox.clear()
        for item in list_of_tickets:
            ticket = '%s - %s' % (item.key, item.fields.summary)
            self.taskActBox.addItem(ticket)

    def start(self):
        if self.clock_started:
            self.timer.stop()
            self.button_start.setText(_translate("MainWindow", "START", None))
            self.clock_started = False
        else:
            global s, m, h
            self.timer.start(1000)
            self.button_start.setText(_translate("MainWindow", "STOP", None))
            self.clock_started = True

    def Time(self):
        global s, m, h

        if s < 59:
            s += 1
        else:
            if m < 59:
                s = 0
                m += 1
            elif m == 59 and h < 24:
                h += 1
                m = 0
                s = 0
            else:
                self.timer.stop()

        time = "{:02d}:{:02d}:{:02d}".format(h, m, s)

        self.lcd.setDigitCount(len(time))
        self.lcd.display(time)

    def reset(self):
        global s, m, h

        self.timer.stop()
        s = 0
        m = 0
        h = 0
        time = "{:02d}:{:02d}:{:02d}".format(h, m, s)
        self.lcd.setDigitCount(len(time))
        self.lcd.display(time)

    def log_task(self):
        self.dialog.exec_()


class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.append("This is a QTextBrowser!")

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.buttonBox)