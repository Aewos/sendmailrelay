# sendmailrelay
SMTP Relay using sendmail-like tools to send email

# Dependencies
Sendmail relay need Python in version 3.* (it did not work with Python 2 at this time).

A Sendmail-compatible tool must be installed. In the default configuration we use msmtp that allow to use user defined configuration.

# SendmailRelay configuration

At this time, you have to change the sendmailrelay code to change de configuration of the sendmailrelay server (it must be changed later). It means that you need some (small) knowledge in python to configure this tool.

The port option is used to set the listen port for the smtp server (the port than SendmailRelay listen).

The opt option is used to add parameters to the sendmail-like command. For exemple, if you use msmtp (as it's the case in the default configuration), set opt=['-a','gmail'] allow to use the "gmail" account defined in the msmtp configuration.

# Run SendmailRelay as deamon

An init.d script (in the init.d directory) is defined. You have to change the user (USER) who launch the server and the working directory (WORKINGDIR) where the sendmailrelay.py file is.
