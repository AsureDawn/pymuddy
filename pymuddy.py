#-*- coding: utf-8 -*-

import os, sys

import telnetlib
from collections import deque
from gi.repository import Gtk,Gdk

import proto
import uxevents

# Dict for text queues of command history
commandhist = {}

# Create main builder, create window in builder
mainbldr = Gtk.Builder()
mainbldr.add_from_file('builder/mainwindow.ui')

# Hook-up signals
signals = {
    'on_window_destroy' : Gtk.main_quit,
    'on_click_openworld': uxevents._openWorld,
    'on_click_newworld' : uxevents._newWorld,
    'on_commandentry_activate': uxevents._activateCommandEntry
}
mainbldr.connect_signals(signals)

# Get all the window objects I'll be modifying
mainwindow = mainbldr.get_object('window1')
mapbuffer = mainbldr.get_object('mapbuffer')

# Still not sure if this is how I want to handle map drawing...
mapbuffer.insert_at_cursor('Hello world!     \n'*10)

mainwindow.show()

Gtk.main()
