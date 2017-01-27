import os
import json
import r2pipe
        
b = os.listdir("/opt/dionaea/var/dionaea/binaries/")
dic = {}
for bin in b:
        r2 = r2pipe.open("/opt/dionaea/var/dionaea/binaries/"+bin)

        r2.cmd('aa')
        a = (r2.cmd('ixx'))
        with open("output.log", "a") as outfile:
                outfile.write(a)
                outfile.close

file = open("output.log", "r")
for line in file:
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
