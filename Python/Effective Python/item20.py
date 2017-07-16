# -*- coding: utf-8 -*-

from datetime import datetime
from time import sleep

def log(message, when = None):
    '''
    Log a message with a timestamp.
    :param message: a message
    :param when: time
    :return: None
    '''
    when = datetime.now()
    print('{0} : {1} '.format(when, message))

log('Hi there!')

sleep(1.5)

log('Hi again!')