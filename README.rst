SSHit
=====

Want to share a terminal session with someone? ::

    $ sshit
    SSH Server started. u: kreitz  p: 3r83r8

    This localtunnel service is brought to you by Twilio.
    Port 2222 is now publicly accessible from http://4jn4.localtunnel.com ...

Send it to the other guy, and he can login::

    $ ssh kreitz@4jn4.localtunnel.com
    kreitz@4jn4.localtunnel.com's password:

Any commands he runs will be be in your sshit stdout.

When you're done having someone in your system, hit Control-C, and the server
is gone.


Powered By
----------

- `localtunnel <http://progrium.com/localtunnel/>`_
- SSH - not sure. Twisted Conch maybe.