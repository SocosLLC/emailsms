emailsms
===========

Module for sending SMS via email SMS gateways. Requires an email account to
send from, and for the phone service provider of the recipient to be known.

Email SMS gateways are unreliable at best. This is not a suitable method for
sending texts for any production use. This is, however, a free and easy way
to prototype SMS-based services.


Usage
-----

::

    >>> yahoo_smtp_server = "smtp.mail.yahoo.com"
    >>> import emailsms
    >>> import smtplib
    >>> from_address = 'foo@gmail.com
    >>> smtp = smtplib.SMTP(yahoo_smtp_server, 587)
    >>> smtp.starttls()
    >>> smtp.login(username, password)
    >>> smtp = emailsms.gmail_smtp(from_address, 'password')
    >>> emailsms.send(smtp, from_address, '0000000000', "Hi it's me", 'Verizon')
    >>> print emailsms.carriers



Contributing
------------

Pull requests welcome!
https://github.com/SocosLLC/emailsms


About Socos
-----------

Socos LLC is the company behind `Muse <https://muse.socoslearning.com>`_.

Muse brings your child's everyday experiences to life and supports
their development through research-based activities. Muse gives you
insights into your child's development and shows you what you can do
each day to support their growth.

