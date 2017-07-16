# -*- coding: utf-8 -*-

from datetime import datetime
from time import sleep

import json

def log(message, when = None):
    '''
    Log a message with a timestamp.
    :param message: a message
    :param when: time
    :return: None
    '''
    when = datetime.now()
    print('{0} : {1} '.format(when, message))

def decode(data, default = None):
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

if __name__ == "__main__":
    foo = decode("bad data")
    foo['stuff'] = 5
    bar = decode("also bad")
    bar['meet'] = 1
    print(foo)
    print(bar)


#log('Hi there!')
#sleep(1.5)
#log('Hi again!')


