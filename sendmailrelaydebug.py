#!/usr/bin/python3
#
#	Author : Adrien Kerfourn
#	Licence : LGPL v3
#

import smtpd
import asyncore
import subprocess

from sendmailrelay import SendmailRelay

class SendmailRelayDebug(SendmailRelay):
	def process_message(self, peer, mailfrom, rcpttos, data):
		print("Message received from :", peer)
		print("From:", mailfrom)
		print("To:", rcpttos)
		print("--- MESSAGE BEGIN ---")
		print(data)
		print("--- MESSAGE END ---\n\n")

if __name__=='__main__':
	import os, sys, traceback
	print("Program started with PID = ", str(os.getpid()))
	try:
		server = SendmailRelayDebug(port=1026)
		asyncore.loop()
	except Exception as e:
		print("Server stop with the following error(s) :")
		print(e)
		print(traceback.print_exc(file=sys.stdout))
	finally:
		server.close()
