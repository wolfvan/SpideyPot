import os
import json
import r2pipe
        
b = os.listdir("/opt/dionaea/var/dionaea/binaries/")
dic = {}

os.system("ls /opt/dionaea/var/dionaea/binaries/ >> testtt.txt")


while 1:

	os.system("ls /opt/dionaea/var/dionaea/binaries/ >> reg_dio.txt")
	os.system("ls /var/log/hontel/ >> reg_hontel.txt")
	filea = open("reg_dio.txt", "r")
	fileb = open("reg_hontel.txt", "r")
	where = filea.tell()
	line = filea.readline()
	if not line:
		time.sleep(1)
		filea.seek(where)
	else:

                if "EXEC" in line:
                        line2 = line.split("     ")
                        type =  line2[1]
                        dic["type"]=type[:-1]
                        #print "type: "+type
                        #print dic
                elif "arch" in line:
                        line2 = line.split("     ")
                        arch =  line2[1][:-1]
                        dic["arch"]=arch
                elif "machine" in line:
                        line2 = line.split("  ")
                        machine =  line2[1]
                        dic["machine"]= machine[:-1]
                elif "os" in line:
                        line2 = line.split("       ")
                        os =  line2[1]
                        dic["os"]= os[:-1]
                elif "compiled" in line:
                        line2 = line.split(" ")
                        compiled =  line2[1:]
                        dic["compiled"]= compiled[:-1]
                elif "file" in line:
                        line2 = line.split(" ")
                        file =  line2[1]
                        dic["file"]= file[:-1]
                        #print "type: "+type
                	print dic
