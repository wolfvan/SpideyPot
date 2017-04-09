import sys
import requests
import time
import os
import logging

LOG_FILENAME = "spideypot.log"

class bot:
    def __init__(self, token, chat_id):
        self.token = "bot351510771:AAHj4t9zBHsh1WA_s1j0vLATF7K2by4lD2M"
        self.chat_id = 144383810
        text = "Results of Mirai"

    def sendPostMessage(self, text):
       	r = requests.post('https://api.telegram.org/' + self.token + '/sendMessage', data = {'text': text, 'chat_id': self.chat_id})
        return r



def main():
	logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
	logging.debug("[+] Starting SpideyPot")
	while 1:
		logging.debug("[+] Checking...")
		daemon()
		time.sleep(600)

def daemon():
	binaries = os.listdir("/var/log/hontel")
	for i in binaries:
		try:
			md5 = i.split("_")[1]
		except:
			pass
		flag = checkRegistry(md5)
			


def checkRegistry(md5):
	flag = 0
	f = open("registry.txt", "r")
	for line in f:
		if md5 in line:
			flag = 1
	if flag == 0:
		logging.debug("[+] New Sample Found "+ md5)
		md5Write(md5)
		sendTel(md5)
	return flag


def md5Write(md5):
	f = open("registry.txt", "a")
	f.write(md5+"\n")


def sendTel(md5):
    logging.debug("[+] Sending Telegram...")
    a = bot(1,2)
    a.sendPostMessage(md5)


if __name__ == "__main__":
	main()
