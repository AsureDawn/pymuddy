#-*- coding:utf-8 -*-

import sys

from collections import deque
import telnetlib as tnl
import select
import socket

class Mud(tnl.Telnet):

    """MUD client class.

    An instance of this class handles communication with a MUD
    server over Telnet.

    Output may be written to a file descriptor of your choosing,
    or to stdout if none is specified.

    listener()
        Just overwrote to change stdout to self.fdout
    """

    def __init__(self, host=None, port=0,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
                 fdout=sys.stdout):
        tnl.Telnet.__init__(self, host, port, timeout)

        # File descriptor to write output to
        self.fdout = fdout

    def interact(self):
        if sys.platform == "win32":
            self.mt_interact()
            return
        while True:
            rfd, wfd, xfd = select.select([self, sys.stdin], [], [])
            if self in rfd:
                try:
                    text = self.read_eager()
                except EOFError:
                    print('*** Connection closed by remote host ***')
                    break
                if text:
                    self.fdout.write(text.decode('ascii'))
                    self.fdout.flush()
            if sys.stdin in rfd:
                line = sys.stdin.readline().encode('ascii')
                if not line:
                    break
                self.write(line)

    def listener(self):
        while True:
            try:
                data = self.read_eager()
            except EOFError:
                print('*** Connection closed by remote host ***')
                return
            if data:
                self.fdout.write(data.decode('ascii'))
            else:
                self.fdout.flush()
