# -*- coding: utf-8 -*-

"""
sshit.core
~~~~~~~~~~

This module contains the primary functionality of sshit.
"""

import random

ALPHABET = 'abcdefghijklmnoprstuvwyxzABCDEFGHIJKLMNOPRSTUVWXYZ'


def random_password(length=6):
    """Returns a random ASCII password of given length."""

    p = ''.join([random.choice(ALPHABET) for i in range(length)])
    return p

