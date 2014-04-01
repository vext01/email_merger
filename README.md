# email_merger


##  Overview

email_merger is a simple program for sending out customised e-mails, using
Makefile-esque substitution on a template e-mail, to multiple addresses.


## Detailed description

email_merger is a simple program for sending out customised e-mails. It
takes in a template e-mail and a TSV (Tab Separated Value) substitution
file. The field names in the TSV file are substituted, using Makefile-esque
syntax, in the template e-mail. Multiple e-mails can be sent, and each
e-mail can be addressed to multiple people. E-mails are sent using the
local sendmail program.

The template file should be a properly formatted e-mail message e.g. one or
more headers followed by a blank line and then the message body.
Substitution can occur in both the header and message body. A sample
template file looks as follows:

```
From: Firstname Lastname 
To: ${EMAIL}
Subject: Test

Dear ${NAME},

Blah blah blah
```

Keys are identified in the template file by the syntax ${X} where X is a
name satisfying the following regular expression [_0-9a-zA-Z]+.

The substitution file starts with a tab separated list of substitution names
which define keys which will be replaced in the template. Each subsequent
line of the substitution file specifies particular values for these keys.
Blank lines in the substitution file are ignored. A new e-mail will be
generated and sent for each line in the substitution file.

```
NAME	EMAIL
Fred	fred@a.com
Bill	bill@z.com
```

If the -e flag is specified, each substituted e-mail is then passed to
$EDITOR for editing. The user may edit any part of the e-mail, including the
headers.

After substitution and any subsequent editing has occurred, the following
headers are added to the outgoing e-mail if they are not present in after
substitution:

```
Date: <date>
User-Agent: email_merger 0.07 (2007/04/08)
```

Note that if BCC header(s) are specified, they are stripped before the
e-mail is sent.

Flags:

  * -d: Dummy run. Do everything except send e-mails.
  * -e: Individually edit each e-mail with $EDITOR before it is sent.
  * -o <dir>: Save each e-mail being sent into dir.

## Customisation

email_merger can be customised via the optional $HOME/.email_merger file,
which is a normal Python file. The following variables may be set:

  * sendmail. Default: /usr/sbin/sendmail -oem -oi
    The location of the sendmail binary. To send e-mail via a remote
    machine, one can use ssh e.g:
	  /usr/bin/ssh -q -C -l myusername remote.com /usr/sbin/sendmail -oem -oi

  * post_sendmail_delay. Default: 1
    The length of time to delay, in seconds, after sending each e-mail.

##  Install
 
email_merger requires Python 2.7. No external libs are required.

email_merger can be run from the source dir or installed by distutils as follows:

```
$ python2.7 setup.py install
```
