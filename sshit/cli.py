# -*- coding: utf-8 -*-

"""
sshit.cli
~~~~~~~~~

This module contains the command-line interface for sshit.
"""

import sys

from clint import args
from clint.textui import colored, indent, puts


def display_version():
    print '{0}. {1}'.format(
        colored.red('sshit'),
        colored.black('A Kenneth Reitz Project.'))


def main():

    # Arumengs were passed.
    if args.get(0) is not None:
        display_version()
        sys.exit(1)

    print 'SSH Server started. u: {0}  p: {1}'.format(
        colored.yellow('kreitz'),
        colored.yellow('iwefhoihef')
    )



