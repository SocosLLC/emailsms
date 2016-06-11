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
https://bitbucket.org/socos_me/emailsms


About Socos
-----------

Socos LLC is the only organization currently taking naturalistic student experiences as the basis for
assessments. The solution to improving education and the learning gap is to close the educational
loop, and provide relevant feedback to educators and parents on what they can do in naturalistic
setting to improve life-outcomes. 

Learn more at http://www.socoslearning.com/
