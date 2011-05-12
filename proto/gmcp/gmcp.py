#-*- coding:utf8 -*-

from collections import deque

import json

data = {}
pingqueue = deque([], 5)
pingavg = None

def sendRequest(server, message):
    # Do client->server mojo here
    pass

def receiveMsg(message):
    try:
        # convert json to native python object
        msgobj = json.load(message)
    except ValueError as e:
        print(e)

    for key in msgobj.iterkeys():
        if key == 'Core':
            if msgobj[key].has_key('Ping'):
                # calculate + store ping avg
                # pingqueue.append(<ping>)
                # pingavg = sum(pingqueue) / len(pingqueue)
                pass
            if msgobj[key].has_key('Goodbye'):
                # Begin disconnection routine
                print(msgobj[key]['Goodbye'])
        elif key == 'Char':
            if msgobj['Char'].has_key('Skills'):
                if msgobj[key]['Skills'].has_key('List'):
                    pass
                if msgobj[key]['Skills'].has_key('Info'):
                    pass
            if msgobj['Char'].has_key('Items'):
                if msgobj[key][charkey].has_key('List'):
                    # do something with list of items
                    # (e.g. Print it, or display list in sidebar)
                    pass
                if msgobj[key][charkey].has_key('Add'):
                    # notify player of new item, or add it to list in sidebar
                    pass
                if msgobj[key][charkey].has_key('Update'):
                    # Update inventory item attributes
                    pass
                if msgobj[key][charkey].has_key('Remove'):
                    # notify player of item removed, or remove...
                    pass

        elif key == 'Comm':
            if msgobj[key].has_key('Players'):
                # display list of players and the channels they share with you
                pass
            if msgobj[key].has_key('Start'):
                # Trigger comm flag and begin handling communications
                # from channel; end previous communications if necessary.
                pass
            if msgobj[key].has_key('End'):
                # End communications from channel
                pass
        elif key == 'Room':
            if msgobj[key].has_key('WrongDir'):
                # Raise dialog, or passively notify user of bad direction
                pass
        elif key == 'Redirect':
            if msgobj[key].has_key('Redirect'):
                if msgobj[key]['Redirect'].has_key('Window'):
                    # redirect output to window specified, if applicable
                    pass
        elif key == 'IRE':
            if msgobj[key].has_key('Rift'):
                if msgobj[key]['Rift'].has_key('List'):
                    # Store rift(s) contents/amounts/descriptions
                    pass
                if msgobj[key]['Rift'].has_key('Change'):
                    # Change a single rift's amount
                    pass
            if msgobj[key].has_key('Composer'):
                if msgobj[key]['Composer'].has_key('Edit'):
                    # Open editor window
                    pass
    if isinstance(msgobj, dict):
        data.update(msgobj)
