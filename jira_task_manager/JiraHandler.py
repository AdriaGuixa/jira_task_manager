'''
Created on 01/12/2017

@author: FV4AGI0
'''

import logging
import jira
import sys
import JiraConstants

class JiraHandler(jira.JIRA):
    '''
    classdocs
    '''

    # Utilities
    def _create_http_basic_session(self, username, password, timeout=None):
        verify = self._options['verify']
        self._session = jira.resilientsession.ResilientSession()
        self._session.verify = verify
        self._session.auth = (username, password)
        self._session.cert = self._options['client_cert']
        try:
            self._session.proxies = self._options['proxies']
        except KeyError:
            logging.info('No proxies in this session.')

    def search_tickets(self, jql_query):
        '''
        Customized search of tickets in Jira

        :param jql_query (str): The JQL query used to find the tickets
        :return: List: all the tickets that matched the JQL query
        '''
        return self.search_issues(jql_str=jql_query) #, fields=JiraConstants.TICKET_FIELDS)

    def add_worklog_time(self, issue, time = None, comment = None):
        '''
        Customized add worklog method to add time spend in the activity

        :param issue: the issue to add the worklog to
        :param time: a worklog entry with this amount of time spent, e.g: 2d
        :param comment: optional worklog comment
        '''

        self.add_worklog(self, issue, timeSpent=time, timeSpentSeconds=None, adjustEstimate=None,
                    newEstimate=None, reduceBy=None, comment=comment, started=None, user=None)
