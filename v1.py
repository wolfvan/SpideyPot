import datetime
import date
import elasticsearch
import os
import r2pipe

def main()
	chk()


def chk():
	binaries= []
	dirs = [“/opt/dionaea/var/binaries/”, “/var/log/hontel/”]
	while 1:
		for dir in dirs:
			a1 = os.listdir(dir)
			for i in a1:
				if i not in binaries:
					anal_bin(dir+i)
					binaries.append(i)
			
		sleep(60)


def anal_bin(bin):
	anl = r2pipe.open(bin)
	infor = anl.cmd("ixxj")
	ctime = generate_time
	infor_time = append_time(infor, ctime)
	export_json(infor)


def generate_time(bin):
	import datetime
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime(“%Y-%m-%d %H:%M:%S”)
	return st

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
