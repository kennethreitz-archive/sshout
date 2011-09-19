# -*- coding: utf-8 -*-

"""
sshout.tmpsshd
~~~~~~~~~~~~~~

This module contains

"""

import sys

from clint import args
from clint.textui import colored

from .core import random_password


def show_info():
    print '{0}. {1}.'.format(
        colored.red('tmpsshd'),
        colored.black('A Kenneth reitz Project')
    )

def show_usage():
    print 'Usage: {0}'.format(
        colored.blue('tmpsshd <username> [<password>]')
    )


def main():

    username = args.not_flags.get(0)
    password = args.not_flags.get(1)

    if not username:
        show_info()
        print
        show_usage()
        sys.exit(1)

    if not password:
        password = random_password()
        # print 'Password: {0}'.format(password)

    print 'Running SSH Server on port 5022.'
    print 'Username: {0}; Password: {1}'.format(username, password)
    print

    from twisted.internet import reactor
    from .ssh import bootstrap
    SSHFactory = bootstrap(username, password)
    reactor.listenTCP(5022, SSHFactory())
    reactor.run()

