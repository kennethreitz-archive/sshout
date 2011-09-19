SSHout: Let is all out.
=======================

Want to share a terminal session with someone? ::

    $ sshit kreitz
    SSH Server started. u: kreitz  p: 3r83r8

    This localtunnel service is brought to you by Twilio.
    Port 5022 is now publicly accessible from http://4jn4.localtunnel.com ...

Send it to the other guy, and he can login::

    $ ssh kreitz@4jn4.localtunnel.com
    kreitz@4jn4.localtunnel.com's password:

When you're done having someone in your system, hit Control-C, and the
server is gone forever.


Powered By
----------

- `localtunnel <http://progrium.com/localtunnel/>`_
- SSH - not sure. Twisted Conch maybe.