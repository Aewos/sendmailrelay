#!/usr/bin/python3
#
#	Author : Adrien Kerfourn
#	Licence : LGPL v3
#

import smtpd
import asyncore
import subprocess

DEFAULT_SENDMAIL_CMD = ["msmtp", "-t"]

class SendmailRelay(smtpd.SMTPServer):

	def __init__(self,port=25,sendmail=DEFAULT_SENDMAIL_CMD,opt=None,localaddr="127.0.0.1"):
		smtpd.SMTPServer.__init__(self,(localaddr,port), None)
		self.sendmail = sendmail
		self.options = []
		if opt is not None:
			for e in opt:
				if (type(e) is str) and (len(e) > 0):
					self.options.append(e)	
		print("Listening on port "+str(port))

	def process_message(self, peer, mailfrom, rcpttos, data):
		if peer[0] in ('127.0.0.1','localhost'):
			cmd = self.sendmail
			cmd.extend(self.options)
			print("Sending email to ", rcpttos)
			process = subprocess.Popen(cmd, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			try:
				(stdoutdata, stderrdata) = process.communicate(input=bytes(data,'UTF-8'))
			except:
				print("[ERROR]: Sendmailrelay is unable to communicate with Sendmail client.")
			finally:
				if len(stdoutdata) > 0:
					print(stdoutdata)
				if len(stderrdata) > 0:
					print(stderrdata)
					print("Email NOT sent due to error :(")
				else:
					print("Email sent without any error :)")

if __name__=='__main__':
	import os, sys, traceback
	print("Program started with PID = ", str(os.getpid()))
	try:
		server = SendmailRelay(port=3673)
		asyncore.loop()
	except Exception as e:
		print("Server stop with the following error(s) :")
		print(e)
		print(traceback.print_exc(file=sys.stdout))
	finally:
		server.close()
