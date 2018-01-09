'''
Created on 01/12/2017

@author: FV4AGI0
'''
from PyQt4 import QtGui
import logging
import sys
import JiraConstants
from JiraHandler import JiraHandler
from jira.exceptions import JIRAError
import time
import TimeManagerGUI
import getpass

s = 0
m = 0
h = 0

class TimeManager(QtGui.QMainWindow, TimeManagerGUI.Ui_MainWindow):

    def __init__(self, parent = None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('GetJiraTickets')
        self.init_time= None
        self.jira = None
        self.list_of_tickets = {}
        self.set_user(getpass.getuser())
        self.button_login.clicked.connect(self.initialize)

    def initialize(self):
        try:
            #self.jira = JiraHandler({'server': JiraConstants.JIRA_HOST},
            #                         basic_auth=(self.usedEdit.text(), 'Lamoreneta'))#self.passEdit.text()))
            self.enable_buttons()
            self.add_task_types(JiraConstants.TASK_TYPE_LIST)

            #self.initialize_tickets()

            self.box_task_type.currentIndexChanged.connect(self.task_activity_selected)
            self.task_activity_selected()

        except JIRAError as e:
            if e.status_code == 401:
                QtGui.QErrorMessage(self, 'Login to JIRA failed')
                self.logger.warn('Login to JIRA failed. Check your username and password')

    def initialize_tickets(self):
        for item in JiraConstants.TASK_TYPE_LIST:
            self.list_of_tickets[item] = self.jira.search_tickets(JiraConstants.TASK_DESCRIPTION[item])


    def task_activity_selected(self):
        self.add_task_activities(self.list_of_tickets[str(self.box_task_type.currentText())])

    def get_list_of_tickets(self):
        return self.list_of_tickets

    def start_counter(self):
        self.init_time = time.time()

    def stop_counter(self):
        end_time = time.time() - self.init_time

    def set_digital_count(self, time):
        self.lcd.setDigitCount(len(time))
        self.lcd.display(time)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = TimeManager()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

if __name__ == '__main__':
    main()