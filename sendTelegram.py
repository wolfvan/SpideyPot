import sys
import requests
import time
import os


class bot:
    def __init__(self, token, chat_id):
        self.token = "bot351510771:AAHj4t9zBHsh1WA_s1j0vLATF7K2by4lD2M"
        self.chat_id = 351510771
        text = "Results of Mirai"

    def sendPostMessage(self, text):
       	r = requests.post('https://api.telegram.org/' + self.token + '/sendMessage', data = {'text': text, 'chat_id': self.chat_id})
        return r




def main():
	while 1:
		daemon()
		sleep(600)

def daemon():
	binaries = os.listdir("/var/log/hontel")
	for i in binaries:
		try:
			md5 = i.split("_")[1]
		except:
			pass
		flag = checkRegistry(md5)
		if flag == 0:
			mdWrite(md5)
			sendTel(md5)


def checkRegistry(md5):
	flag = 0
	f = open("registry.txt", "r")
	for line in f:
		if md5 in line:
			flag = 1
	if flag == 0:
		md5Write(md5)
	return flag


def md5Write(md5):
	f = open("registry.txt", "a")
	f.write(md5)


def sendTel(md5):
    a = bot(1,2)
    a.sendPostMessage(f.read())


if __name__ == "__main__":
	main()
