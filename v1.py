import datetime
import date
import elasticsearch
import os
import r2pipe
import json

def main():
	chk()


def chk():
	binaries= []
	dirs = [“/opt/dionaea/var/binaries/”, “/var/log/hontel/”]
	while 1:
		for dir in dirs:
			a1 = os.listdir(dir)
			for i in a1:
				if in_registry(i):
					anal_bin(dir+i)
					
			
		sleep(60)

def in_registry(i):
	flag = False
	f = open("registry.log", "r")
	for line in f:
		if i in line:
			flag = True
	f.close
	if flag == True:
		f1 = open("registry.log", "w")
		f1.write(i)
		f1.close()

	return flag

def anal_bin(bin):
	anl = r2pipe.open(bin)
	infor = anl.cmd("ixxj")
	inforj = json.loads(infor)
	ctime = generate_time
	infor_time = append_time(inforj, ctime)
	#export_json(infor)
	write_json(infor)


def generate_time(bin):
	import datetime
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime(“%Y-%m-%d %H:%M:%S”)
	return st

def write_json(infor):
	f = open("write_json")

def append_time(infor, ctime):
	with open(infor, mode = “w”, encoding = “utf-8”) as j:
		json.dump([], j)
		actime = {“timestamp” : ctime}
		k.append(actime)
		json.dump(k, j)
	return j

def export_json(infor):

	res.index(index= “binaries_honeypot”, doc_type= “json”, id=1, body=infor)


if __init__ == "__main__":
	main()	
