'''
Created on 01/12/2017

@author: FV4AGI0
'''

JIRA_HOST = 'http://10.201.235.10:8080'

TICKET_FIELDS = ','.join([
    'project',
    'summary',
    'SQA Task Type'
])

SQATP = 'project = SQATP AND status != Done'
CUSTOM_ASSIGNEE = '(assignee in (currentUser()) OR watcher in (currentUser()))'

RELEASE_ACTIVITY = '"SQA Task Type" = Validation'
CUSTOMER_SUPPORT = '"SQA Task Type" = Support'
PRE_VALIDATION = '"SQA Task Type" = Pre-validation'
IMPROVEMENT = '"SQA Task Type" = Improvement'

TASK_TYPE_LIST = [
    'Validation Activity',
    'Pre-validation',
    'Customer Support',
    'Improvement',
    'Generic'
]

TASK_DESCRIPTION = {
    'Validation Activity': '%s AND %s AND %s' % (SQATP, CUSTOM_ASSIGNEE, RELEASE_ACTIVITY),
    'Customer Support':'%s AND %s AND %s' % (SQATP, CUSTOM_ASSIGNEE, CUSTOMER_SUPPORT),
    'Pre-validation': '%s AND %s AND %s' % (SQATP, CUSTOM_ASSIGNEE, PRE_VALIDATION),
    'Improvement': '%s AND %s AND %s' % (SQATP, CUSTOM_ASSIGNEE, IMPROVEMENT),
    'Generic': 'key = SQATP-8160'
}